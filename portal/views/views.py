from django.urls import reverse
from django.views import View, generic
from django.shortcuts import redirect
from django.shortcuts import resolve_url
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from portal.forms import LoginForm, SingUpForm, ProfileUpdateForm, SubjectForm, EnrollSubjectForm, SectionForm
from portal.models.profiles import Profile
from portal.models.subjects import Subject, EnrollSubject
from portal.models.students import Certificate, Section, Project
