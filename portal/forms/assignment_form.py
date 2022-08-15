from django.forms import ModelForm, TextInput, Select
from portal.models import Assignment, Mark
from portal.models import Subject


class AssignmentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AssignmentForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.filter(department=user.department)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field
            }
            self.fields['subject'].widget.attrs = {
                'class': 'form-control',
                'id': field
            }

    class Meta:
        model = Assignment
        fields = ('title', 'subject', 'assignment_file')