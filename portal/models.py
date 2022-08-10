from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf import settings

User = settings.AUTH_USER_MODEL


class TimeStamp(models.Model):
    """ Abstract timestamp models"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        abstract = True


class Faculty(TimeStamp):
    """Faculty can be submitted only admin"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Department(TimeStamp):
    """Department can be submitted only admin"""
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subject(TimeStamp):
    """ Marks can be submitted admin and update and delete """
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True)
    code = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Semester(TimeStamp):
    """ Semester can be submitted only admin """
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='semesters')
    session = models.CharField(max_length=100)
    year = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} -> {self.session}'


class Ebook(TimeStamp):
    """ Marks can be submitted teacher and update or admin """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    book_cover_image = models.ImageField(upload_to='book-cover/',
                                         validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], blank=True)
    author_name = models.CharField(max_length=150)
    description = models.TextField(max_length=200, blank=True)
    book_pdf = models.FileField(upload_to='books/', validators=[FileExtensionValidator(['pdf'])], max_length=5242880)

    def __str__(self):
        return self.name


class EnrollSubject(TimeStamp):
    """ Marks can be submitted student and approve admin """
    subjects = models.ManyToManyField(Subject, related_name='subjectEnroll')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    is_approve = models.BooleanField(verbose_name='Do you want to approve', default=False)

    def __str__(self):
        return self.student.email


class Routine(TimeStamp):
    """ Marks can be submitted teacher and update or admin """
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_routine')
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
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_certificate')
    certificate_title = models.CharField(max_length=250)
    certificate = models.FileField(upload_to='ssc_certificate/', help_text='Image format must be jpg/jpeg or png',
                                    validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'pdf'])])


class Project(TimeStamp):
    """ Marks can be submitted student and update and delete """
    student = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    project_url = models.CharField(max_length=250, blank=True)
    project_file = models.FileField(upload_to='projects/', help_text='Project file format must .zip',
                                    validators=[FileExtensionValidator(['zip'])], null=True, blank=True)


class Assignment(TimeStamp):
    """ Assignment can be uploaded and delete student """
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignment_students')
    title = models.CharField(max_length=150)
    assignment_file = models.FileField(upload_to='assignment/', validators=[FileExtensionValidator(['pdf'])])


class Mark(TimeStamp):
    """ Marks can be submitted teacher and update or admin """
    STATUS_CHOICES = (
        ('Assignment', 'Assignment'),
        ('Attendance', 'Attendance'),
        ('Midterm', 'Midterm'),
        ('Class Test', 'Class Test'),
        ('Final', 'Final')
    )
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teacher_marks')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_marks')
    marks = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, default='Assignment', max_length=20)


class Notice(TimeStamp):
    """ Notice can be submitted only admin update and delete """
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='notice/',
                              validators=[FileExtensionValidator(['jpg', 'jpeg'])])

    class Meta:
        verbose_name = 'Notice'
        verbose_name_plural = 'Notices'

    def __str__(self):
        return self.title
