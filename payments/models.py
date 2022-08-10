from django.db import models
from portal.models import TimeStamp, Semester
from users.models import Student


class Payment(TimeStamp):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    paid = models.DecimalField(max_digits=10, decimal_places=2)
    due = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.student.username
