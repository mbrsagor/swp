from django.contrib.auth.models import User
from django.db import models
from .teachers import DomainEntity


class Subject(DomainEntity):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=120, unique=True)
    code = models.IntegerField(help_text='subject code must have 3 digit')

    def __str__(self):
        return self.name


class EnrollSubject(DomainEntity):
    is_approve = models.BooleanField(default=False)
    subjects = models.ManyToManyField(Subject, related_name='subjectEnroll')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')

    def __str__(self):
        return self.student.username