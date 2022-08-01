from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings
from .domain_entity import DomainEntity
from portal.models.subject import Subject

User = settings.AUTH_USER_MODEL


class Notice(DomainEntity):
    """
    Notice can be submitted only admin update and delete
    """
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    notice_file = models.ImageField(upload_to='notice/',
        validators=[FileExtensionValidator(['jpg', 'jpeg'])])

    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    def __str__(self):
        return self.title

class Faculty(DomainEntity):
    """Faculty can be submitted only admin"""
    title = models.CharField(max_length=255)

class Department(DomainEntity):
    """Department can be submitted only admin"""
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)


class Semester(DomainEntity):
    """
    Semester can be submitted only admin
    """
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='semesters')
    session = models.CharField(max_length=100)
    year = models.DateField()
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)


class Financial_Data(DomainEntity):
    """
    Financial data can be submitted onlys admin update and delete. student can see you data.
    """
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    paid = models.DecimalField()
    unpaid = models.DecimalField()
