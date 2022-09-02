from django.forms import (
    TextInput,
    PasswordInput,
    CharField,
    BooleanField,
)
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': 'username or email', 'required': True,
               'autofocus': True}))
    password = CharField(
        widget=PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True}))
    remember_me = BooleanField(required=False)