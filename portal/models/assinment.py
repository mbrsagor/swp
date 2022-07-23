from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from .domain_entity import DomainEntity


class Assignment(DomainEntity):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Completed', 'Completed'),
        ('Incompleted', 'Incompleted')
    )
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=200)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignment_students')
    status = models.CharField(choices=STATUS_CHOICES, default='Active', max_length=20)
    assignment_file = models.FileField(upload_to='assignment/', validators=[FileExtensionValidator(['pdf'])])

    @property
    def pass_mark(self):
        return self.mark_assignments.pass_mark


class Mark(DomainEntity):
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
    pass_mark = models.IntegerField(default='33')
    status = models.CharField(choices=STATUS_CHOICES, default='Assignment', max_length=20)


class Report(DomainEntity):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=200)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_teacher')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='report_assignment')
    is_active = models.BooleanField(default=True)
