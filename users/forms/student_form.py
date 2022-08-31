from datetime import datetime
from django.forms import (
    ModelForm,
    TextInput,
    EmailInput,
    Select,
    PasswordInput,
    CharField,
    DateInput,
    FileInput,
    EmailField,
    ChoiceField,
    ModelChoiceField,
    DateField,
    NumberInput,
    ValidationError
)
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from users.models import Student, StudentProfile
from faculties.models import Faculty, Department, Program


class StudentSingUpForm(UserCreationForm):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    )

    SESSION_CHOICES = (
        ('SPRING', 'SPRING'),
        ('SUMMER', 'SUMMER'),
    )

    email = EmailField(widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    username = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    faculty = ModelChoiceField(queryset=Faculty.objects.all(), widget=Select(attrs={'class': 'form-control'}))
    department = ModelChoiceField(queryset=Department.objects.all(), widget=Select(attrs={'class': 'form-control'}))
    program = ModelChoiceField(queryset=Program.objects.all(), widget=Select(attrs={'class': 'form-control'}))
    session = ChoiceField(widget=Select(attrs={'class': 'form-control'}), choices=SESSION_CHOICES)
    gender = ChoiceField(widget=Select(attrs={'class': 'form-control'}), choices=GENDER)
    full_name = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}))
    father_name = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Father name'}))
    mother_name = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother name'}))
    date_of_birth = DateField(widget=DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    ssc_passing_year = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'SSC passing year'}))
    hsc_passing_year = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'HSC passing year'}))
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter valid password'}))
    password2 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'}))

    class Meta(UserCreationForm.Meta):
        model = Student

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        age = (datetime.date(datetime.now()) - dob).days / 365
        if age < 18:
            raise ValidationError('Must be at least 18 years old to register')
        return dob

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.save()
        profile = StudentProfile.objects.create(user=user)
        profile.faculty = self.cleaned_data.get('faculty')
        profile.department = self.cleaned_data.get('department')
        profile.program = self.cleaned_data.get('program')
        profile.session = self.cleaned_data.get('session')
        profile.full_name = self.cleaned_data.get('full_name')
        profile.father_name = self.cleaned_data.get('father_name')
        profile.mother_name = self.cleaned_data.get('mother_name')
        profile.ssc_passing_year = self.cleaned_data.get('ssc_passing_year')
        profile.hsc_passing_year = self.cleaned_data.get('hsc_passing_year')
        profile.date_of_birth = self.cleaned_data.get('date_of_birth')
        profile.gender = self.cleaned_data.get('gender')
        profile.save()
        return user


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('username', 'email')

        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'id': 'username', 'placeholder': 'Enter your username'}),
            'email': EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter your email'}),
        }


class StudentProfileForm(ModelForm):

    class Meta:
        model = StudentProfile
        fields = '__all__'
        exclude = ('user',)

        widgets = {
            'faculty': Select(attrs={'class': 'form-control', 'id': 'faculty'}),
            'department': Select(attrs={'class': 'form-control', 'id': 'department'}),
            'program': Select(attrs={'class': 'form-control', 'id': 'program'}),
            'session': Select(attrs={'class': 'form-control', 'id': 'session'}),
            'full_name': TextInput(attrs={'class': 'form-control', 'id': 'full_name'}),
            'roll_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'student roll number format 001-101', 'id': 'roll_number'}),
            'unique_id': TextInput(attrs={'class': 'form-control', 'id': 'unique_id'}),
            'father_name': TextInput(attrs={'class': 'form-control', 'id': 'father_name'}),
            'mother_name': TextInput(attrs={'class': 'form-control', 'id': 'mother_name'}),
            'cgpa': NumberInput(attrs={'step': 0.25, 'class': 'form-control', 'id': 'cgpa'}),
            'gender': Select(attrs={'class': 'form-control', 'id': 'gender'}),
            'date_of_birth': DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'date_of_birth'}),
            'ssc_passing_year': TextInput(attrs={'class': 'form-control', 'id': 'ssc_passing_year'}),
            'hsc_passing_year': TextInput(attrs={'class': 'form-control', 'id': 'hsc_passing_year'}),
            'avatar': FileInput(attrs={'class': 'form-control', 'id': 'avatar'}),
            'credit': NumberInput(attrs={'step': 0.25, 'class': 'form-control', 'id': 'credit'}),
        }
