from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from swp.models import TimeStamp
from users.managers import UserManager
from faculties.models import Faculty, Department, Program


class User(AbstractBaseUser, PermissionsMixin):

    class Rolls(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        STUDENT = 'STUDENT', 'Student'
        TEACHER = 'TEACHER', 'Teacher'

    default_type = Rolls.ADMIN

    username = models.CharField(max_length=155, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    roll = models.CharField(choices=Rolls.choices, default=default_type, max_length=7, db_index=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def student(self):
        return self.roll == self.Rolls.STUDENT

    @property
    def teacher(self):
        return self.roll == self.Rolls.TEACHER

    @property
    def admin(self):
        return self.roll == self.Rolls.ADMIN

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        if not self.id:
            self.roll = self.default_type
        return super().save(*args, **kwargs)

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True

    # def get_absolute_url(self):
    #     return reverse('accounts:dashboard_view', kwargs={'pk': self.pk})


class StudentProfile(TimeStamp):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    )
    MAX_CREDIT = 10
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    roll_number = models.CharField(max_length=5, blank=True, help_text='student id format 001-101',)
    unique_id = models.CharField(max_length=16, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True)
    avatar = models.ImageField(upload_to='student-avatar/', max_length=524288)
    name = models.CharField(max_length=50, blank=True)
    father_name = models.CharField(max_length=50, blank=True)
    mother_name = models.CharField(max_length=50, blank=True)
    board_roll = models.CharField(max_length=100, blank=True)
    ssc_passing_year = models.DateField(blank=True, null=True)
    hsc_passing_year = models.DateField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    cgpa = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    gender = models.CharField(choices=GENDER, max_length=10, blank=True)
    is_updated = models.BooleanField(default=False)

    @property
    def avatarURL(self):
        return self.avatar.url if self.avatar else '/static/image/avatar.png'

    # @property
    # def credit(self):
    #     return self.my_course_schedule.


class TeacherProfile(TimeStamp):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    avatar = models.ImageField(upload_to='book-avatar/', max_length=524288)
    gender = models.CharField(choices=GENDER, max_length=10, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, blank=True)

    @property
    def avatarURL(self):
        return self.avatar.url if self.avatar else '/static/image/avatar.png'


class AdminProfile(TimeStamp):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='admin_profile')
    avatar = models.ImageField(upload_to='book-avatar/', max_length=524288)
    gender = models.CharField(choices=GENDER, max_length=10, blank=True)

    @property
    def avatarURL(self):
        return self.avatar.url if self.avatar else '/static/image/avatar.png'


class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(roll=User.Rolls.STUDENT)


class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(roll=User.Rolls.TEACHER)


class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(roll=User.Rolls.ADMIN)


class Admin(User):
    default_type = User.Rolls.TEACHER
    objects = AdminManager()

    class Meta:
        proxy = True

    @property
    def profile(self):
        return self.adminprofile


class Teacher(User):
    default_type = User.Rolls.TEACHER
    objects = TeacherManager()

    class Meta:
        proxy = True

    @property
    def profile(self):
        return self.teacherprofile


class Student(User):
    default_type = User.Rolls.STUDENT
    objects = StudentManager()

    class Meta:
        proxy = True

    @property
    def profile(self):
        return self.studentprofile



