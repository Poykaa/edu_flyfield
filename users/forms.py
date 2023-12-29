from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class SignUpForm(UserCreationForm):
    role_choice = [
        ('Teacher', 'Викладач'),
        ('Student', 'Учень')
    ]
    role = forms.ChoiceField(choices=role_choice)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role')