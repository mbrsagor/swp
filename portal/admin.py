from django.contrib import admin
from portal.models import Certificate, Project, Mark, Ebook


admin.site.register([Certificate, Project, Mark, Ebook])
