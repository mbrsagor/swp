from django.contrib import admin
from .models.profile import Profile
from .models.subject import Subject, EnrollSubject
from .models.student import Certificate, Section, Project
from .models.assinment import Assignment, Report

admin.site.register([Profile, Subject, EnrollSubject, Certificate, Section, Project, Assignment, Report])
