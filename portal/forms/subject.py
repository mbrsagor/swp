from django.forms import ModelForm, TextInput, NumberInput, CheckboxInput, CheckboxSelectMultiple, SelectMultiple
from portal.models.subject import Subject, EnrollSubject


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
