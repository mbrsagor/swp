from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings
from .domain_entity import DomainEntity

User = settings.AUTH_USER_MODEL


class Routine(DomainEntity):
    """
    Marks can be submitted teacher and update or admin
    """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_routine')
    title = models.CharField(max_length=150, unique=True)
    routine_image = models.ImageField(upload_to='routine/',
                                      validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'pdf'])])

    class Meta:
        verbose_name = 'Routine'
        verbose_name_plural = 'Routines'

    def __str__(self):
        return self.title
