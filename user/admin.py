from django.contrib import admin
from user.models import User, Assessment, Submission, Grade


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'role', 'is_superuser']
    list_display_links = ['id', 'username']
    list_filter = ['email']
    search_fields = ['username', 'email']


admin.site.register(User, UserModelAdmin)


class AssessmentAdminModel(admin.ModelAdmin):
    list_display = ['id', 'mentor', 'title', 'date_line', 'created_at']
    list_display_links = ['id', 'mentor']
    list_filter = ['title', 'date_line']
    search_fields = ['title', 'date_line']


admin.site.register(Assessment, AssessmentAdminModel)


class SubmissionAdminModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'assessment', 'link', 'file', 'created_at', 'updated_at']
    list_display_links = ['id', 'user']
    list_filter = ['assessment', 'user']
    search_fields = ['link', 'file', 'assessment']


admin.site.register(Submission, SubmissionAdminModel)


class GradeAdminModel(admin.ModelAdmin):
    list_display = ['id', 'mentor', 'submission', 'grade', 'created_at']
    list_display_links = ['id', 'mentor']
    list_filter = ['submission', 'grade']
    search_fields = ['mentor', 'submission', 'grade']


admin.site.register(Grade, GradeAdminModel)
