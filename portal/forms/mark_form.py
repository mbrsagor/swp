from django.forms import ModelForm, Select, TextInput
from portal.models import Mark
from faculties.models import CourseSchedule
from users.models import Student


class MarkForm(ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(MarkForm, self).__init__(*args, **kwargs)
        if user.teacher:
            self.fields['course_schedule'].queryset = CourseSchedule.objects.filter(teacher=user)
        else:
            self.fields['course_schedule'].queryset = CourseSchedule.objects.all()

    class Meta:
        model = Mark
        fields = ('student', 'course_schedule', 'marks', 'status')

        widgets = {
            'student': Select(attrs={'class': 'form-control', 'id': 'student'}),
            'course_schedule': Select(attrs={'class': 'form-control', 'id': 'course_schedule'}),
            'marks': TextInput(attrs={'type': 'number', 'class': 'form-control', 'id': 'name'}),
            'status': Select(attrs={'class': 'form-control', 'id': 'status'}),
        }


class MarkUpdateForm(ModelForm):
    class Meta:
        model = Mark
        fields = ('marks', 'status')

        widgets = {
            'marks': TextInput(attrs={'type': 'number', 'class': 'form-control', 'id': 'name'}),
            'status': Select(attrs={'class': 'form-control', 'id': 'status'}),
        }
