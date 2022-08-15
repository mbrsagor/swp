from django.forms import (
    ModelForm,
    TextInput,
    EmailInput,
    Select,
    PasswordInput,
    CharField,
    DateInput,
    BooleanField,
    SelectMultiple,
    CheckboxSelectMultiple,
    ImageField,
)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User, Teacher, Student, StudentProfile, TeacherProfile
from portal.models import Subject


class LoginForm(AuthenticationForm):
    username = CharField(widget=TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your username', 'required': True,
               'autofocus': True}))
    password = CharField(
        widget=PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password', 'required': True}))
    remember_me = BooleanField(required=False)


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'department')

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'department': Select(attrs={'class': 'form-control', 'id': 'department'}),
        }


class StudentSingUpForm(UserCreationForm):
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter valid password'}))
    password2 = CharField(
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}))

    class Meta:
        model = Student
        fields = ('username', 'email', 'department')

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'department': Select(attrs={'class': 'form-control', 'id': 'department'}),
        }


class TeacherSingUpForm(UserCreationForm):
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter valid password'}))
    password2 = CharField(
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}))

    class Meta:
        model = Teacher
        fields = ('username', 'email', 'department')

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'department': Select(attrs={'class': 'form-control', 'id': 'department'}),
        }


class StudentProfileForm(ModelForm):

    class Meta:
        model = StudentProfile
        fields = (
            'name', 'father_name', 'mother_name', 'board_roll', 'cgpa', 'gender',
            'date_of_birth', 'ssc_passing_year', 'hsc_passing_year', 'avatar',
        )

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'father_name': TextInput(attrs={'class': 'form-control', 'id': 'father_name'}),
            'mother_name': TextInput(attrs={'class': 'form-control', 'id': 'mother_name'}),
            'board_roll': TextInput(attrs={'class': 'form-control', 'id': 'board_roll'}),
            'cgpa': TextInput(attrs={'class': 'form-control', 'id': 'cgpa'}),
            'gender': Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'date_of_birth': DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'date_of_birth'}),
            'ssc_passing_year': DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'ssc_passing_year'}),
            'hsc_passing_year': DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'hsc_passing_year'})
        }


class TeacherProfileForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(TeacherProfileForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.filter(department=self.request.user.department)

    class Meta:
        model = TeacherProfile
        fields = (
            'subject',
            'avatar',
            'gender',
        )

        widgets = {
            'subject': CheckboxSelectMultiple(attrs={'class': 'flat-red', 'id': 'subjects'}),
            'gender': Select(attrs={'class': 'form-control', 'id': 'gender'}),
        }