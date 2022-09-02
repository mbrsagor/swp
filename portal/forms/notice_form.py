from django.forms import ModelForm, TextInput, FileInput
from portal.models import Notice


class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'
        exclude = ('admin',)

        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'id': 'title'}),
            'image': FileInput(attrs={'class': 'form-control', 'id': 'image'})
        }
