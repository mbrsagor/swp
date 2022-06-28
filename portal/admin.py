from django.contrib import admin
from .models.profiles import Profile
from .models.subjects import Subject
from .models.students import Certificate, Section, Project

admin.site.register([Profile, Subject, Certificate, Section, Project])
