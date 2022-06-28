from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm, CharField, EmailInput, TextInput, Select, PasswordInput, BooleanField, \
    NumberInput, DateTimeInput, CheckboxInput, SelectMultiple, CheckboxSelectMultiple, FileInput

from django.contrib.auth.models import User
from .models.profiles import Profile
from .models.subjects import Subject, EnrollSubject
from .models.students import Certificate, Section, Project


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


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = (
            '__all__'
        )
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'code': NumberInput(attrs={'class': 'form-control', 'id': 'code'}),
            'is_active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
        }


class EnrollSubjectForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EnrollSubjectForm, self).__init__(*args, **kwargs)
        self.fields["subjects"].widget = CheckboxSelectMultiple(attrs={'class': 'flat-red'})
        self.fields["subjects"].queryset = Subject.objects.all()

    class Meta:
        model = EnrollSubject
        read_only_fields = ('student',)
        fields = (
            '__all__'
        )
        widgets = {
            'subjects': SelectMultiple(attrs={'class': 'form-control', 'id': 'subjects'}),
            'is_active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
        }


class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
        exclude = ('student',)

    def __init__(self, *args, **kwargs):
        super(CertificateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
                'placeholder': f'Enter {field}'
            }


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
                'placeholder': f'Enter {field}'
            }
            self.fields['is_active'].widget = CheckboxInput(attrs={'class': 'form-check-input', 'id': field, })


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ('student',)

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
                'placeholder': f'Enter {field}'
            }
