from django.forms import ModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import CharField, TextInput, PasswordInput, BooleanField, DateTimeInput
from users.models import User, Profile


class SingUpForm(UserCreationForm):
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter valid password'}))
    password2 = CharField(
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}))

    class Meta:
        model = User
        fields = (
            'id', 'full_name', 'email',
        )

    def __init__(self, *args, **kwargs):
        super(SingUpForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
                'placeholder': f'Enter {field}'
            }

            self.fields['email'].widget.attrs['placeholder'] = 'Enter a valid email address'
            self.fields['password1'].widget.attrs['placeholder'] = 'Enter valid password'
            self.fields['password2'].widget.attrs['placeholder'] = 'Enter confirm password'



class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        read_only_fields = ('user',)
        fields = (
            'name', 'father_name', 'mother_name', 'board_roll', 'cgpa', 'gender',
            'date_of_birth', 'ssc_passing_year', 'hsc_passing_year',
        )

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
                'placeholder': f'Enter {field}'
            }

            self.fields['date_of_birth'].widget = DateTimeInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'id': field,
                'type': 'date'
            })
            self.fields['ssc_passing_year'].widget = DateTimeInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'id': field,
                'type': 'date'
            })
            self.fields['hsc_passing_year'].widget = DateTimeInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'id': field,
                'type': 'date'
            })