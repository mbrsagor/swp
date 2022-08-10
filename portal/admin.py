from django.contrib import admin
from portal.models import Subject, EnrollSubject, Certificate, Project,  Assignment, Mark, Faculty, Department


admin.site.register([Subject, EnrollSubject, Certificate, Project, Assignment, Mark, Faculty, Department])
