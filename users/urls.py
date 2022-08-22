from django.urls import path
from users.views import auth_view, student_view, teacher_view, dashboard_view

app_name = "users"
urlpatterns = [
    path("", dashboard_view.DashboardView.as_view(), name="dashboard"),
    path("dashboard/", dashboard_view.DashboardView.as_view(), name="dashboard"),
    # Auth
    path("login/", auth_view.SingInView.as_view(), name="login"),
    path("logout/", auth_view.SignOutView.as_view(), name="logout"),
    path("registration/", student_view.RegistrationView.as_view(), name="registration"),
    # Profile
    path("profiles/<pk>/", student_view.StudentProfileView.as_view(), name="profiles"),
    path("profiles/<pk>/update/", student_view.ProfileUpdateView.as_view(), name="profiles-update"),
    # students
    path("students/", student_view.StudentListView.as_view(), name="students"),
    path("students/create/", student_view.StudentCreateView.as_view(), name="students-create"),
    path("students/<pk>/update/", student_view.StudentUpdateView.as_view(), name="students-update"),
    path("students/<pk>/delete/", student_view.StudentDeleteView.as_view(), name="students-delete"),
    # teachers
    path("teachers/", teacher_view.TeacherListView.as_view(), name="teachers"),
    path("teachers/profile/<pk>/", teacher_view.TeacherProfileView.as_view(), name="teachers-profile"),
    path("teachers/profile/<pk>/update/", teacher_view.TeacherProfileUpdateView.as_view(),
         name="teachers-profile-update"),
    path("teachers/create/", teacher_view.TeacherCreateView.as_view(), name="teachers-create"),
    path("teachers/<pk>/update/", teacher_view.TeacherUpdateView.as_view(), name="teachers-update"),
    path("teachers/<pk>/delete/", teacher_view.TeacherDeleteView.as_view(), name="teachers-delete"),
]
