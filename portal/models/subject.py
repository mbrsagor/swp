from django.db import models
from django.conf import settings
from .domain_entity import DomainEntity

User = settings.AUTH_USER_MODEL


class Subject(DomainEntity):
    """
    Marks can be submitted admin and update and delete
    """
    name = models.CharField(max_length=120, unique=True)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class EnrollSubject(DomainEntity):
    """
    Marks can be submitted student and approve admin
    """
    subjects = models.ManyToManyField(Subject, related_name='subjectEnroll')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    is_approve = models.BooleanField(verbose_name='Do you want to approve', default=False)

    def __str__(self):
        return self.student.email