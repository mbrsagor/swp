from django.forms import ModelForm
from portal.models.routine import Routine

class RoutineForm(ModelForm):
    class Meta:
        model = Routine
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RoutineForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
                'placeholder': f'Enter {field}'

            }