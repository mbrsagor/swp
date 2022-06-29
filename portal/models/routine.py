from django.db import models
from .domain_entity import DomainEntity


class Routine(DomainEntity):
    title = models.CharField(max_length=150, unique=True)
    routine_image = models.ImageField(upload_to='routine/')

    class Meta:
        verbose_name = 'Routine'
        verbose_name_plural = 'Routines'

    def __str__(self):
        return self.title
