from django.db import models
from swp.models import TimeStamp
from faculties.models import Semester
from users.models import Student


class Payment(TimeStamp):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    paid = models.IntegerField(default=0)
    due = models.IntegerField(default=0)

    def __str__(self):
        return self.student.username
