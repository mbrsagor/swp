from django.forms import (
    ModelForm,
    TextInput,
    EmailInput,
    Select,
    PasswordInput,
    CharField,
    DateInput,
    FileInput,
)
from django.contrib.auth.forms import UserCreationForm
from users.models import Student, StudentProfile


class StudentSingUpForm(UserCreationForm):
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter valid password'}))
    password2 = CharField(
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}))

    class Meta:
        model = Student
        fields = ('username', 'email')

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        }


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('username', 'email')

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Enter your username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter your email'}),
        }


class StudentProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(StudentProfileForm, self).__init__(*args, **kwargs)
        profile = StudentProfile.objects.get(user=user)
        if profile.is_updated:
            for field in self.fields:
                self.fields[field].disabled = True


    class Meta:
        model = StudentProfile
        fields = '__all__'
        exclude = ('user', 'student_id')

        widgets = {
            'faculty': Select(attrs={'class': 'form-control', 'id': 'faculty'}),
            'department': Select(attrs={'class': 'form-control', 'id': 'department'}),
            'program': Select(attrs={'class': 'form-control', 'id': 'program'}),
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'father_name': TextInput(attrs={'class': 'form-control', 'id': 'father_name'}),
            'mother_name': TextInput(attrs={'class': 'form-control', 'id': 'mother_name'}),
            'board_roll': TextInput(attrs={'class': 'form-control', 'id': 'board_roll'}),
            'cgpa': TextInput(attrs={'class': 'form-control', 'id': 'cgpa'}),
            'gender': Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'date_of_birth': DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'date_of_birth'}),
            'ssc_passing_year': DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'ssc_passing_year'}),
            'hsc_passing_year': DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'hsc_passing_year'}),
            'avatar': FileInput(attrs={'class': 'form-control', 'id': 'avatar'}),
        }
