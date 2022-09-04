from django.contrib import admin
from faculties.models import (
    Faculty,
    Department,
    Program,
    Semester,
    Course,
    Assignment,
    AssignmentSubmit
)

admin.site.register([Faculty, Department, Program, Semester, Course, Assignment, AssignmentSubmit])
