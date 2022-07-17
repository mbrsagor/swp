from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from .domain_entity import DomainEntity


class Ebook(DomainEntity):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    book_cover_image = models.ImageField(upload_to='book-cover/',
                                         validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    author_name = models.CharField(max_length=150)
    description = models.TextField(max_length=200)
    book_pdf = models.FileField(upload_to='books/', validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return self.name
