from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('full_name', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('full_name', 'email')
    readonly_fields = ('pk',)
    filter_horizontal = []
    ordering = ('email',)
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'roll', 'password1', 'password2'),
        }),
    )