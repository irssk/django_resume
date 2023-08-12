from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
import os


def valifator_lvl(value):
    if 0 < value > 10:
        raise ValidationError(
            _("%(value)s is not an even number"), 
            params={"value": value})
    
def valifator_month(value):
    if 0 < value > 60:
        raise ValidationError(
            _("%(value)s is not an even number"), 
            params={"value": value})

def avatar_wrapper(instance:object, filename:str):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format('avatar', ext)
    
    if Avatar.objects.get(image=f"images/avatar/{filename}"):
        Avatar.objects.get(image=f"images/avatar/{filename}").image.delete(save=True)
        
    return os.path.join('images/avatar', filename)


class Avatar(models.Model):
   image = models.ImageField(upload_to=avatar_wrapper)
   

class Skill(models.Model):
    name = models.CharField(max_length=50)
    lvl = models.IntegerField(validators=[valifator_month])
    
    def __str__(self):
        return self.name     
   
class About(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(editable=True)
    story = models.TextField(editable=True)
    photo = models.ImageField(upload_to='images/photo')
    skills = models.ManyToManyField(Skill)
    slug = models.CharField(max_length=72, editable=False, auto_created=True)
    
    def save(self):
        self.slug = slugify(self.title)
        super().save()
    
    def __str__(self):
        return f"{self.title}"


class Galery(models.Model):
    image = models.ImageField(upload_to='images/galery')
    about = models.ForeignKey(About, on_delete=models.CASCADE)


class Education(models.Model):
    organization = models.CharField(max_length=30)
    type_of_education = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    how_many_month = models.IntegerField(validators=[valifator_month])
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.organization} - {self.type_of_education}"


class Projects(models.Model):
    title = models.CharField(max_length=30)
    discription = models.TextField()
    image = models.ImageField(upload_to='images/projects')
    url = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=72, editable=False, auto_created=True)
    
    def save(self):
        self.slug = slugify(self.title)
        super().save()
        
    def __str__(self):
        return f'{self.title}'