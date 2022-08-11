from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from django.db.models import ForeignKey

from users.managers import UserManager
from portal.models import Department, Subject


class User(AbstractBaseUser, PermissionsMixin):

    class Rolls(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        STUDENT = 'STUDENT', 'Student'
        TEACHER = 'TEACHER', 'Teacher'

    default_type = Rolls.ADMIN

    username = models.CharField(max_length=155, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, blank=True)
    roll = models.CharField(choices=Rolls.choices, default=default_type, max_length=7, db_index=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

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


class StudentProfile(models.Model):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    )
    gender = models.CharField(choices=GENDER, max_length=10, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    name = models.CharField(max_length=50, blank=True)
    father_name = models.CharField(max_length=50, blank=True)
    mother_name = models.CharField(max_length=50, blank=True)
    board_roll = models.CharField(max_length=100, blank=True)
    ssc_passing_year = models.DateField(blank=True, null=True)
    hsc_passing_year = models.DateField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    cgpa = models.DecimalField(max_digits=5, decimal_places=2, default=1.00)


class TeacherProfile(models.Model):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    gender = models.CharField(choices=GENDER, max_length=10, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)


class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(roll=User.Rolls.STUDENT)


class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(roll=User.Rolls.TEACHER)


class Teacher(User):
    default_type = User.Rolls.TEACHER
    objects = TeacherManager()

    class Meta:
        proxy = True

    def profile(self):
        return self.teacherprofile

class Student(User):
    default_type = User.Rolls.STUDENT
    objects = StudentManager()

    class Meta:
        proxy = True

    def whoami(self):
        print('I am a Student.')

    @property
    def profile(self):
        return self.studentprofile



