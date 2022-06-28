from django.urls import path
from portal.views import students
from portal.views import teachers
from portal.views import subjects
from portal.views import auth
from portal.views import sections


urlpatterns = [
    path('', auth.DashboardView.as_view(), name='dashboard'),
    path('dashboard/', auth.DashboardView.as_view(), name='dashboard'),
    # Auth
    path('login/', auth.SingInView.as_view(), name="login"),
    path('logout/', auth.SignOutView.as_view(), name='logout'),
    path('registration/', auth.RegistrationView.as_view(), name='registration'),
    # Profile
    path('profile/', auth.ProfileView.as_view(), name="profile"),
    path('profile-update/<pk>/', auth.ProfileUpdateView.as_view(), name="profile_update"),
    # Subject
    path('subject/', subjects.SubjectCreateListView.as_view(), name="subject_create_listview"),
    path('subject/delete/<pk>/', subjects.SubjectDeleteView.as_view(), name="subject_delete"),
    path('subject-enroll/', subjects.EnrollSubjectView.as_view(), name="subject_enroll"),
    # section
    path('section/', sections.SectionView.as_view(), name='section_view'),
    path('section-delete/<pk>/', sections.SectionDeleteView.as_view(), name='section_delete_view'),
    # student
    path('certificates/', students.CertificateListAndCreateView.as_view(), name='certificates_view'),
    path('certificates-delete/<pk>/', students.CertificateDeleteView.as_view(), name='certificates_delete_view'),
]
