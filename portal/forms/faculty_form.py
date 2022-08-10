from django.forms import ModelForm, TextInput, Select, DateInput
from portal.models import Faculty, Department, Semester
from users.models import Student


class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields = ('name',)

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
        }


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ('faculty', 'name')

        widgets = {
            'faculty': Select(attrs={'class': 'form-control', 'id': 'faculty'}),
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
        }


class SemesterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SemesterForm, self).__init__(*args, **kwargs)
        self.fields['student'].queryset = Student.objects.all()

    class Meta:
        model = Semester
        fields = '__all__'
        exclude = ('created_at', 'updated_at')

        widgets = {
            'student': Select(attrs={'class': 'form-control', 'id': 'student'}),
            'session': TextInput(attrs={'class': 'form-control', 'id': 'session'}),
            'year': DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'year'}),
            'department': Select(attrs={'class': 'form-control', 'id': 'department'}),
        }

