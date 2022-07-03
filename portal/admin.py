from django.contrib import admin
from .models.profile import Profile
from .models.subject import Subject
from .models.student import Certificate, Section, Project

admin.site.register([Profile, Subject, Certificate, Section, Project])
