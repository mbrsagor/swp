from django.db import models
from .domain_entity import DomainEntity


class Notice(DomainEntity):
    title = models.CharField(max_length=255)
    announcement = models.TextField()
    is_published = models.BooleanField(default=True)
    notice_file = models.FileField(upload_to='notice/',null=True,blank=True)

    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    def __str__(self):
        return self.title
