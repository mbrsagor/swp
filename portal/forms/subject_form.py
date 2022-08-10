from django.forms import ModelForm, TextInput, CheckboxInput, CheckboxSelectMultiple, SelectMultiple, Select
from portal.models import Subject, EnrollSubject
from portal.models import Department


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = (
            '__all__'
        )
        widgets = {
            'department': Select(attrs={'class': 'form-control', 'id': 'department'}),
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'code': TextInput(attrs={'class': 'form-control', 'id': 'code'}),
            'is_active': CheckboxInput(attrs={'class': 'form-check-input ml-2', 'id': 'is_active'}),
        }


class EnrollSubjectForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(EnrollSubjectForm, self).__init__(*args, **kwargs)
        # department = Department.objects.filter()
        self.fields["subjects"].widget = CheckboxSelectMultiple(attrs={'class': 'flat-red'})
        self.fields["subjects"].queryset = Subject.objects.filter(department=self.request.user.department)

    class Meta:
        model = EnrollSubject
        fields = ('subjects',)
        widgets = {
            'subjects': SelectMultiple(attrs={'class': 'form-control', 'id': 'subjects'})
        }
