from django.forms import ModelForm
from portal.models import Routine


class RoutineForm(ModelForm):
    class Meta:
        model = Routine
        fields = ('title', 'routine_image')

    def __init__(self, *args, **kwargs):
        super(RoutineForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
            }
