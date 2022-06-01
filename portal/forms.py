from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, CharField, EmailInput, TextInput, Select, PasswordInput, BooleanField, \
    CheckboxInput, NumberInput, Textarea, DateTimeInput, FileInput

from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your username', 'required': True,
               'autofocus': True}))
    password = CharField(
        widget=PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True}))
    remember_me = BooleanField(required=False)


class SingUpForm(UserCreationForm):
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter valid password'}))
    password2 = CharField(
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}))

    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'first_name', 'last_name'
        )
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Enter username'}),
            'email': EmailInput(
                attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter valid a valid email'}),
            'first_name': TextInput(
                attrs={'class': 'form-control', 'id': 'first_name', 'placeholder': 'Enter first name'}),
            'last_name': TextInput(
                attrs={'class': 'form-control', 'id': 'last_name', 'placeholder': 'Enter last name'}),
        }
