from django.db import models
from django.core.validators import FileExtensionValidator
from swp.models import TimeStamp
from users.models import Student, Teacher, Admin
from faculties.models import CourseSchedule


class Ebook(TimeStamp):
    """ Marks can be submitted book and update or admin """
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    book_cover_image = models.ImageField(upload_to='book-cover/',
                                         validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], blank=True)
    author_name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    book_pdf = models.FileField(upload_to='books/', validators=[FileExtensionValidator(['pdf'])], max_length=214958080)

    def __str__(self):
        return self.name


class Routine(TimeStamp):
    """ Marks can be submitted book and update or admin """
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='my_routine')
    title = models.CharField(max_length=150, unique=True)
    routine_image = models.FileField(upload_to='routine/',
                                     validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'pdf'])])

    class Meta:
        verbose_name = 'Routine'
        verbose_name_plural = 'Routines'

    def __str__(self):
        return self.title


class Certificate(TimeStamp):
    """ Marks can be submitted student and update and delete """
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='my_certificate')
    certificate_title = models.CharField(max_length=250)
    certificate = models.FileField(upload_to='ssc_certificate/', help_text='Image format must be jpg/jpeg or png',
                                   validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'pdf'])])


class Project(TimeStamp):
    """ Marks can be submitted student and update and delete """
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_url = models.CharField(max_length=250, blank=True)
    project_file = models.FileField(upload_to='projects/', help_text='Project file format must .zip',
                                    validators=[FileExtensionValidator(['zip'])], null=True, blank=True,
                                    max_length=214958080)


class Mark(TimeStamp):
    """ Marks can be submitted book and update or admin """
    STATUS_CHOICES = (
        ('Assignment', 'Assignment'),
        ('Attendance', 'Attendance'),
        ('Midterm', 'Midterm'),
        ('Class Test', 'Class Test'),
        ('Final', 'Final')
    )
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_marks')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_marks')
    course_schedule = models.ForeignKey(CourseSchedule, on_delete=models.CASCADE)
    marks = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, default='Assignment', max_length=20)


class Notice(TimeStamp):
    """ Notice can be submitted only admin update and delete """
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='notice/',
                              validators=[FileExtensionValidator(['jpg', 'jpeg'])])

    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    def __str__(self):
        return self.title
