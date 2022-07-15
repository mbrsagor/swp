from django.contrib.auth.models import User
from django.db import models
from .domain_entity import DomainEntity


class Subject(DomainEntity):
    objects = None
    name = models.CharField(max_length=120, unique=True)
    code = models.IntegerField(help_text='subject code must have 3 digit')
    is_active = models.BooleanField(verbose_name='Do you want to publish', default=True)

    def __str__(self):
        return self.name


class EnrollSubject(DomainEntity):
    subjects = models.ManyToManyField(Subject, related_name='subjectEnroll')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    is_approve = models.BooleanField(verbose_name='Do you want to approve', default=False)

    def __str__(self):
        return self.student.username