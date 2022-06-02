from django.urls import path
from portal import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    # Auth
    path('login/', views.SingInView.as_view(), name="login"),
    path('logout/', views.SignOutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]
