from django.shortcuts import render
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = 'home.hml'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
        


# Create your views here.
