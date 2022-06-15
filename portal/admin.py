from django.contrib import admin
from portal.models import Profile, Subject

admin.site.register([Profile, Subject])
