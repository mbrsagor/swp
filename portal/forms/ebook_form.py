from django.forms import ModelForm, TextInput, Textarea, FileInput, Select
from portal.models import Ebook


class BookForm(ModelForm):
    class Meta:
        model = Ebook
        fields = '__all__'
        exclude = ('teacher',)

        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'book_cover_image': FileInput(attrs={'class': 'form-control', 'id': 'book_cover_image'}),
            'author_name': TextInput(attrs={'class': 'form-control', 'id': 'author_name'}),
            'description': Textarea(attrs={'class': 'form-control', 'id': 'description'}),
            'book_pdf': FileInput(attrs={'class': 'form-control', 'id': 'book_pdf'}),
        }


