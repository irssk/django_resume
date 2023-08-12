from django import forms
from .models import *


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', )


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name', 'lvl',)
        labels = {
            'name': "enter name of skill",
            'lvl': "enter lvl of skill"
        }
        

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ('name', 'description', 'story', 'photo', 'skills')
        labels = {
            'name': 'Enter name and surname', 
            'description': 'Print discriprion if u', 
            'story': 'short story', 
            'photo': 'choose photo', 
            'skills': 'choose skills'
        }
    
    