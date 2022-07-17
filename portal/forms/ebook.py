from django.forms import ModelForm
from portal.models.ebook import ReferenceEbook


class EbookForm(ModelForm):
    class Meta:
        model = ReferenceEbook
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EbookForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field,
                'placeholder': f'Enter {field}'

            }
