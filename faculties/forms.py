from django import forms
from faculties.models import (
    Faculty,
    Department,
    Semester,
    Program,
    Course,
    CourseSchedule,
    Assignment,
    AssignmentSubmit
)
from users.models import Student, Teacher


class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('name', 'code')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'code': forms.NumberInput(attrs={'class': 'form-control', 'id': 'code'})
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('faculty', 'name', 'code')

        widgets = {
            'faculty': forms.Select(attrs={'class': 'form-control', 'id': 'faculty'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'code': forms.NumberInput(attrs={'class': 'form-control', 'id': 'code'})
        }


class SemesterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SemesterForm, self).__init__(*args, **kwargs)
        self.fields['student'].queryset = Student.objects.all()

    class Meta:
        model = Semester
        fields = '__all__'
        exclude = ('created_at', 'updated_at')

        widgets = {
            'student': forms.Select(attrs={'class': 'form-control', 'id': 'student'}),
            'session': forms.Select(attrs={'class': 'form-control', 'id': 'session'}),
            'schedule': forms.Select(attrs={'class': 'form-control', 'id': 'schedule'}),
            'year': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'year'}),
            'batch': forms.TextInput(attrs={'class': 'form-control', 'id': 'batch'}),
            'department': forms.Select(attrs={'class': 'form-control', 'id': 'department'}),
        }


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('department', 'name', 'code')
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control', 'id': 'department'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'code': forms.NumberInput(attrs={'class': 'form-control', 'id': 'code'})
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('program', 'title', 'credit')
        widgets = {
            'program': forms.Select(attrs={'class': 'form-control', 'id': 'program'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'credit': forms.NumberInput(attrs={'class': 'form-control', 'id': 'credit'})
        }


class CourseScheduleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CourseScheduleForm, self).__init__(*args, **kwargs)
        self.fields['teacher'].queryset = Teacher.objects.all()
        self.fields['student'].queryset = Student.objects.all()

    class Meta:
        model = CourseSchedule
        fields = '__all__'

        widgets = {
            'course': forms.Select(attrs={'class': 'form-control', 'id': 'course'}),
            'teacher': forms.Select(attrs={'class': 'form-control', 'id': 'teacher'}),
            'student': forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'student'}),
            'schedule': forms.Select(attrs={'class': 'form-control', 'id': 'schedule'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
        }


class AssignmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AssignmentForm, self).__init__(*args, **kwargs)
        self.fields['course_schedule'].queryset = CourseSchedule.objects.filter(teacher=user)

    class Meta:
        model = Assignment
        fields = ('course_schedule', 'title', 'assignment_file', 'last_date', 'is_active')
        exclude = ('teacher',)

        widgets = {
            'course_schedule': forms.Select(attrs={'class': 'form-control', 'id': 'course_schedule'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'assignment_file': forms.FileInput(attrs={'class': 'form-control', 'id': 'assignment_file'}),
            'last_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'last_date'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
        }


class AssignmentSubmitForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmit
        fields = ('assignment_file_url',)
        exclude = ('student',)

        widgets = {
            'assignment_file_url': forms.URLInput(attrs={'class': 'form-control', 'id': 'assignment_file_url'})
        }


