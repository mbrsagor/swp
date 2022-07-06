from django.forms import ModelForm,CheckboxInput
from portal.models.notice import Notice


class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NoticeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
                'placeholder': f'Enter {field}'

            }
            self.fields['is_published'].widget = CheckboxInput(attrs={'class': 'form-check-input', 'id': field, })
