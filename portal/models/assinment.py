from django.core.validators import FileExtensionValidator
from django.db import models
from django.conf import settings
from .domain_entity import DomainEntity

User = settings.AUTH_USER_MODEL


class Assignment(DomainEntity):
    """
    Assignemnt can be upload and delete student
    """
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignment_students')
    title = models.CharField(max_length=150)
    assignment_file = models.FileField(upload_to='assignment/', validators=[FileExtensionValidator(['pdf'])])


class Mark(DomainEntity):
    """
    Marks can be submitted teacher and update or admin
    """
    STATUS_CHOICES = (
        ('Assignment', 'Assignment'),
        ('Attendance', 'Attendance'),
        ('Midterm', 'Midterm'),
        ('Class Test', 'Class Test'),
        ('Final', 'Final')
    )
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_marks')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_marks')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE,
                                   related_name='mark_assignments', null=True, blank=True)
    marks = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, default='Assignment', max_length=20)
