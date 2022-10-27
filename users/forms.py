from django import forms
from django.contrib.auth.admin.forms import CustomUserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        field = ('username','email','dob','phone')