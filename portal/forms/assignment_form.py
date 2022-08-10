from django.forms import ModelForm
from portal.models import Assignment, Mark


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ('title', 'assignment_file')

    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field
            }
