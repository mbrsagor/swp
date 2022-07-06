from django.db import models
from .domain_entity import DomainEntity


class ReferenceEbook(DomainEntity):
    ebook_title = models.CharField(max_length=150)
    short_desc = models.TextField()
    ebook_file = models.FileField(upload_to='ebooks/')

    class Meta:
        verbose_name = 'E-book'
        verbose_name_plural = 'E-books'

    def __str__(self):
        return self.ebook_title
