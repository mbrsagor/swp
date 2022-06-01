from django.urls import path
from portal import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('signin/', views.SingInView.as_view(), name='login'),
]
