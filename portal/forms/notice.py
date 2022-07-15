from django.forms import ModelForm, CheckboxInput
from ..models.notice import Notice


class NoticeForm(ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'
        exclude = ('admin',)

    def __init__(self, *args, **kwargs):
        super(NoticeForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
            }
            self.fields['is_published'].widget = CheckboxInput(attrs={'class': 'form-check-input ml-2', 'id': field})
