from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import datetime
from swp.models import TimeStamp

User = settings.AUTH_USER_MODEL


# Create your models here.
class Faculty(TimeStamp):
    """Faculty can be submitted only admin"""
    name = models.CharField(_('name'), max_length=255)
    code = models.CharField(_('code'), max_length=10)

    def __str__(self):
        return self.name


class Department(TimeStamp):
    """Department can be submitted only admin"""
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(_('name'), max_length=255)
    code = models.CharField(_('code'), max_length=10)

    def __str__(self):
        return self.name


class Program(TimeStamp):
    """Program can be submitted only admin"""
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='programs')
    name = models.CharField(_('name'), max_length=255)

    def __str__(self):
        return self.name


class Course(TimeStamp):
    """Course can be submitted only admin"""
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(_('title'), max_length=120, unique=True)
    credit = models.FloatField(_('code'))

    def natural_key(self):
        return self.title

    def __str__(self):
        return self.title


class CourseSchedule(TimeStamp):
    SCHEDULE_CHOICES = (
        ('DAY', 'Day'),
        ('EVENING', 'Evening')
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_schedule')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_course_schedule')
    students = models.ManyToManyField(User, blank=True, related_name='my_course_schedule')
    schedule = models.CharField(choices=SCHEDULE_CHOICES, max_length=8)
    is_active = models.BooleanField(default=True)

    @property
    def title(self):
        return self.course.title

    def __str__(self):
        return self.course.title


class Assignment(TimeStamp):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_assignments')
    course_schedule = models.ForeignKey(CourseSchedule, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=150)
    assignment_file = models.FileField(upload_to='assignment/',
                                       validators=[FileExtensionValidator(['pdf'])], max_length=214958080)
    last_date = models.DateField()
    is_active = models.BooleanField(default=True)

    @property
    def date_expiry(self):
        lt = self.last_date
        nt = datetime.now()
        return int(lt.strftime('%Y%m%d')) - int(nt.strftime('%Y%m%d'))

    def __str__(self):
        return self.title


class AssignmentSubmit(TimeStamp):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_assignment_submit')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='assignment_submit')
    assignment_file_url = models.URLField(help_text='github, gitlab or google drive file link')

    @property
    def submitted(self):
        return self.student

    def __str__(self) -> str:
        return f'{self.student}'


class Semester(TimeStamp):
    """Semester can be submitted only admin"""

    SCHEDULE_CHOICES = (
        ('DAY', 'Day (Regular)'),
        ('EVENING', 'Evening')
    )
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='semesters')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    schedule = models.CharField(choices=SCHEDULE_CHOICES, max_length=8)
    year = models.DateField()
    batch = models.CharField(max_length=10)

    def __str__(self):
        return self.schedule
