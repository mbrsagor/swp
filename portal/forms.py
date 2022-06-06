from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, CharField, EmailInput, TextInput, Select, PasswordInput, BooleanField, \
     NumberInput,  DateTimeInput, FileInput

from django.contrib.auth.models import User
from .models import Profile


class LoginForm(AuthenticationForm):
    username = CharField(widget=EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your email', 'required': True,
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


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        read_only_fields = ('user',)
        fields = (
            'user', 'name', 'father_name', 'mother_name', 'board_roll',
            'date_of_birth', 'ssc_passing_year', 'hsc_passing_year',
        )
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'gender': Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'father_name': TextInput(attrs={'class': 'form-control', 'id': 'father_name'}),
            'mother_name': TextInput(attrs={'class': 'form-control', 'id': 'mother_name'}),
            'board_roll': NumberInput(attrs={'class': 'form-control', 'id': 'board_roll'}),
            'date_of_birth': DateTimeInput(attrs={'class': 'form-control', 'id': 'date_of_birth', 'type': 'date'}),
            'ssc_passing_year': DateTimeInput(
                attrs={'class': 'form-control', 'id': 'ssc_passing_year', 'type': 'date'}),
            'hsc_passing_year': DateTimeInput(
                attrs={'class': 'form-control', 'id': 'hsc_passing_year', 'type': 'date'}),
        }
