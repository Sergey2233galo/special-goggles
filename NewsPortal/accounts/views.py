from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SighUpForm

class SighUp(CreateView):
    model = User
    form_class = SighUpForm
    success_url = '/accounts/login'

    template_name = 'registration/sighup.html'
