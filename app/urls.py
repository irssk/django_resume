from django.urls import path

from .views import homepage, avatar_upload, ThankYouView, SkillFormView, AboutFormView


urlpatterns = [
    path('', homepage, name="homepage"),
    path('avatar_upload/', avatar_upload, name="avatar_upload"),
    path('thank-you/', ThankYouView.as_view(), name='thank-you'),
    path('skills_form/', SkillFormView.as_view(), name="skill_form"),
    path('about_form/', AboutFormView.as_view(), name="about_form"),
]
