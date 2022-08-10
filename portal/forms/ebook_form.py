from django.forms import ModelForm
from portal.models import Ebook


class BookForm(ModelForm):
    class Meta:
        model = Ebook
        fields = '__all__'
        exclude = ('teacher',)

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'id': field
            }

