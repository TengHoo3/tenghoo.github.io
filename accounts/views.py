from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from . import forms
from django.shortcuts import render
from django.contrib.auth.models import User

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

def Profile(request):
    return render(request,'accounts/profile.html',context = {
        "User" : User.objects.get(username=request.user.username)
    })