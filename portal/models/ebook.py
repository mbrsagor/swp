from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings
from .domain_entity import DomainEntity

User = settings.AUTH_USER_MODEL


class Ebook(DomainEntity):
    """
    Marks can be submitted teacher and update or admin
    """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    book_cover_image = models.ImageField(upload_to='book-cover/',
                                         validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], blank=True)
    author_name = models.CharField(max_length=150)
    description = models.TextField(max_length=200, blank=True)
    book_pdf = models.FileField(upload_to='books/', validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return self.name
