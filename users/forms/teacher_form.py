from django.forms import (
    ModelForm,
    TextInput,
    EmailInput,
    Select,
    PasswordInput,
    CharField,
    CheckboxSelectMultiple,
)
from django.contrib.auth.forms import UserCreationForm
from users.models import Teacher, TeacherProfile


class TeacherSingUpForm(UserCreationForm):
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter valid password'}))
    password2 = CharField(
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}))

    class Meta:
        model = Teacher
        fields = ('username', 'email')

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        }


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('username', 'email')

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Enter your username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter your email'}),
        }


class TeacherProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(TeacherProfileForm, self).__init__(*args, **kwargs)
        # self.fields['subject'].queryset = Subject.objects.filter(department=self.request.user.department)

    class Meta:
        model = TeacherProfile
        fields = (
            'avatar',
            'gender',
        )

        widgets = {
            'subject': CheckboxSelectMultiple(attrs={'class': 'flat-red', 'id': 'subjects'}),
            'gender': Select(attrs={'class': 'form-control', 'id': 'gender'}),
        }