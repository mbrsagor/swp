from django.forms import ModelForm
from ..models.assinment import Assignment, Report, Mark


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'
        exclude = ('student',)

    def __init__(self, *args, **kwargs):
        super(AssignmentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field
            }


class MarkForm(ModelForm):
    class Meta:
        model = Mark
        fields = '__all__'
        exclude = ('teacher', 'assignment')

    def __init__(self, *args, **kwargs):
        super(MarkForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field
            }


class ReportForm(ModelForm):
    class Meta:
        model = Report
        fields = ('title', 'description')

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field
            }
