from django.forms import ModelForm, CheckboxInput, DateTimeInput
from portal.models import Certificate, Project


class CertificateForm(ModelForm):
    class Meta:
        model = Certificate
        fields = ('certificate_title', 'certificate')

    def __init__(self, *args, **kwargs):
        super(CertificateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
                'placeholder': f'Enter {field}'
            }


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ('title', 'description', 'project_url', 'project_file')

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
                'placeholder': f'Enter {field}'
            }
