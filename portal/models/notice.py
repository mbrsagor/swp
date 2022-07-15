from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from .domain_entity import DomainEntity


class Notice(DomainEntity):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    announcement = models.TextField(max_length=200)
    notice_file = models.FileField(upload_to='notice/', validators=[FileExtensionValidator(['pdf'])], blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    def __str__(self):
        return self.title
