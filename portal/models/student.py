from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings
from .domain_entity import DomainEntity

User = settings.AUTH_USER_MODEL


class Certificate(DomainEntity):
    """
    Marks can be submitted student and update and delete
    """
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_title = models.CharField(max_length=250)
    certificate = models.ImageField(upload_to='ssc_certificate/', help_text='Image format must be jpg/jpeg or png',
                                        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'pdf'])])


class Project(DomainEntity):
    """
    Marks can be submitted student and update and delete
    """
    student = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    project_url = models.CharField(max_length=250, blank=True)
    project_file = models.FileField(upload_to='projects/', help_text='Project file format must .zip',
                                        validators=[FileExtensionValidator(['zip'])])
