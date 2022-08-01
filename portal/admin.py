from django.contrib import admin
from .models.subject import Subject, EnrollSubject
from .models.student import Certificate, Section, Project
from .models.assinment import Assignment, Report, Mark

admin.site.register([Subject, EnrollSubject, Certificate, Section, Project, Assignment, Mark])
