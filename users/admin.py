from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Student, Teacher, StudentProfile, TeacherProfile

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('username', 'email')
    readonly_fields = ('pk',)
    filter_horizontal = []
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'roll', 'password1', 'password2'),
        }),
    )




admin.site.register([Teacher, TeacherProfile, Student, StudentProfile])
