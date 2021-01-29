from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import notes_create
from django import forms

class NewNote(forms.ModelForm):
    class Meta:
        model=notes_create
        fields=['username','note']

class RegisterNewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']
