from django.contrib import admin
from .models.profiles import Profile
from .models.subjects import Subject
from .models.students import Certificate, Section, Project
from .models.routine import Routine
from .models.notice import Notice
admin.site.register([Profile, Subject, Certificate, Section, Project,Routine,Notice])
