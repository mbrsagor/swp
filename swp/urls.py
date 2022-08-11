from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view

# Load static files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal.urls')),
    path('', include('users.urls')),
    path('payments/', include('payments.urls')),
    path("password_reset/", auth_view.PasswordResetView.as_view(template_name='password_reset/password-reset.html'), name="password_reset"),
    path(
        "password_reset/done/",
        auth_view.PasswordResetDoneView.as_view(template_name='password_reset/password-done.html'),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_view.PasswordResetConfirmView.as_view(template_name='password_reset/password-confirm.html'),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_view.PasswordResetCompleteView.as_view(template_name='password_reset/reset-complete.html'),
        name="password_reset_complete",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
