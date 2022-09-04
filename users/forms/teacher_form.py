from django.db import transaction
from django.forms import (
    ModelForm,
    TextInput,
    EmailInput,
    EmailField,
    Select,
    PasswordInput,
    CharField,
    ModelChoiceField,
    ChoiceField, ImageField, FileInput
)
from django.contrib.auth.forms import UserCreationForm
from users.models import Teacher, TeacherProfile
from faculties.models import Department


class TeacherSingUpForm(UserCreationForm):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    )
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter valid password'}))
    password2 = CharField(
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}))
    email = EmailField(widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    username = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    department = ModelChoiceField(queryset=Department.objects.all(), widget=Select(attrs={'class': 'form-control'}))
    gender = ChoiceField(widget=Select(attrs={'class': 'form-control'}), choices=GENDER)
    avatar = ImageField(widget=FileInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = Teacher

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.save()
        profile = TeacherProfile.objects.create(user=user)
        profile.department = self.cleaned_data.get('department')
        profile.avatar = self.cleaned_data.get('avatar')
        profile.gender = self.cleaned_data.get('gender')
        profile.save()
        return user


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ('username', 'email')

        widgets = {
            'username': TextInput(
                attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Enter your username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter your email'}),
        }


class TeacherProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(TeacherProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TeacherProfile
        fields = (
            'department',
            'avatar',
            'gender',
        )

        widgets = {
            'department': Select(attrs={'class': 'form-control', 'id': 'department'}),
            'gender': Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'avatar': FileInput(attrs={'class': 'form-control', 'id': 'avatar'}),
        }
