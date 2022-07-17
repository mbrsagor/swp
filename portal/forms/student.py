from django.forms import ModelForm, CheckboxInput, DateTimeInput
from portal.models.student import Certificate, Section, Project


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
            self.fields['is_active'].widget = CheckboxInput(attrs={'class': 'form-check-input ml-2', 'id': field, })


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
            self.fields['is_active'].widget = CheckboxInput(attrs={'class': 'form-check-input ml-2', 'id': field, })
            self.fields['expiry_date'].widget = DateTimeInput(format='%Y-%m-%d', attrs={
                'class': 'form-control',
                'id': field,
                'type': 'date'
            })
