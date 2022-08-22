from django.forms import ModelForm, Select, TextInput
from portal.models import Mark
from users.models import Student


class MarkForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(MarkForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Mark
        fields = ('student', 'marks', 'status')

        widgets = {
            'student': Select(attrs={'class': 'form-control', 'id': 'student'}),
            'marks': TextInput(attrs={'type': 'number', 'class': 'form-control', 'id': 'name'}),
            'status': Select(attrs={'class': 'form-control', 'id': 'status'}),
        }
