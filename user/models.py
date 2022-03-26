from django.db import models
from django.contrib.auth.models import AbstractUser

from user.utils import ROLE
from user.manager import UserManager


class User(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    role = models.IntegerField(choices=ROLE.get_choices(), default=ROLE.STUDENT.value)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.username


class Assessment(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assessmentMentor')
    title = models.CharField(max_length=120)
    description = models.TextField()
    date_line = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:30]

    @property
    def mentor_name(self):
        return self.mentor.username


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='assessmentSubmission')
    link = models.URLField(max_length=200, blank=True, null=True)
    file = models.FileField(upload_to='submission', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.assessment.title

    @property
    def assessment_name(self):
        return self.assessment.title

    @property
    def submission_user(self):
        return self.user.username


class Grade(models.Model):
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)

    GRADE_LIST = (
        ("G1", "+A"),
        ("G2", "A"),
        ("G3", "-A"),
        ("G4", "B"),
        ("G5", "+B"),
        ("G6", "B"),
        ("G7", "C"),
    )
    grades = models.CharField(max_length=2, choices=GRADE_LIST)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.submission.assessment.title
