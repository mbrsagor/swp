from django.urls import path, re_path
from users import views


urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    # Auth
    path('login/', views.SingInView.as_view(), name="login"),
    path('logout/', views.SignOutView.as_view(), name='logout'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    # Profile
    path('profile/<pk>/', views.StudentProfileView.as_view(), name="profile"),
    path('profile/update/<pk>/', views.ProfileUpdateView.as_view(), name="profile-update"),
    # students
    path('students/', views.StudentListView.as_view(), name='students-view'),
    path('students/create/', views.StudentCreateView.as_view(), name='students-create-view'),
    path('students/update/<pk>/', views.StudentUpdateView.as_view(), name='students-update-view'),
    path('students/delete/<pk>/', views.StudentDeleteView.as_view(), name='students-delete-view'),
    # teachers
    path('teachers/', views.TeacherListView.as_view(), name='teachers-view'),
    path('teachers/profile/<pk>/', views.TeacherProfileView.as_view(), name='teachers-profile-view'),
    path('teachers/profile/update/<pk>/', views.TeacherProfileUpdateView.as_view(),
         name='teachers-profile-update-view'),
    path('teachers/create/', views.TeacherCreateView.as_view(), name='teachers-create-view'),
    path('teachers/update/<pk>/', views.TeacherUpdateView.as_view(), name='teachers-update-view'),
    path('teacher/delete/<pk>/', views.TeacherDeleteView.as_view(), name='teacher-delete-view'),
]