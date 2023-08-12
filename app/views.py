from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import AvatarForm, SkillForm, AboutForm
from .models import Avatar, Skill, About


def homepage(req):
    avatar = Avatar.objects.last()
    return render(req, 'app/app.html', {
        'avatar': avatar
    })
    

def avatar_upload(request):
    
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("../thank-you/")
    
    form = AvatarForm()
    
    avatar = Avatar.objects.last()
    
    return render(request, "app/avatar_form.html", {
        'form': form,
        'avatar': avatar
        })
    
class ThankYouView(TemplateView):
    template_name = 'app/thank-you.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        avatar = Avatar.objects.last()
        context['msg'] = 'Allright!'

        return {'context': context, 'avatar': avatar}
    

class SkillFormView(FormView):
    template_name = "app/skillform.html"
    form_class = SkillForm
    success_url = "../thank-you/"
    
    def form_valid(self, form):
        return super().form_valid(form)
    

class AboutFormView(FormView): 
    template_name = "app/skillform.html"
    form_class = AboutForm
    success_url = "../thank-you/"
    
    def form_valid(self, form):
        return super().form_valid(form)