from django.db import models
from .domain_entity import DomainEntity
from django.contrib.auth.models import User


class Certificate(DomainEntity):
    student = models.OneToOneField(User, on_delete=models.PROTECT)
    ssc_certificate = models.FileField(upload_to='ssc_certificate/')
    hsc_certificate = models.FileField(upload_to='hsc_certificate/')
    cv = models.FileField(upload_to='cv/')


class Section(DomainEntity):
    name = models.CharField(max_length=150, db_index=True)
    description = models.TextField(max_length=250)
    is_active = models.BooleanField(verbose_name='Do you want to publish', default=True)


class Project(DomainEntity):
    student = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    project_url = models.CharField(max_length=250)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    expiry_date = models.DateTimeField(verbose_name='expiry date')
    is_active = models.BooleanField(verbose_name='Do you want to publish', default=True)
