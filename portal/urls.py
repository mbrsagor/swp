from django.urls import path
from portal.views import student
from portal.views import teacher
from portal.views import subject
from portal.views import auth
from portal.views import section


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
    path('subject/', subject.SubjectCreateListView.as_view(), name="subject_create_listview"),
    path('subject/delete/<pk>/', subject.SubjectDeleteView.as_view(), name="subject_delete"),
    path('subject-enroll/', subject.EnrollSubjectView.as_view(), name="subject_enroll"),
    # section urls
    path('section/', section.SectionView.as_view(), name='section_view'),
    path('section-delete/<pk>/', section.SectionDeleteView.as_view(), name='section_delete_view'),
    # certificate urls
    path('certificates/', student.CertificateListAndCreateView.as_view(), name='certificates_view'),
    path('certificate-detail/<pk>/', student.CertificateUpdateAndDetailView.as_view(), name='certificate_detail_update_view'),
    path('certificates-delete/<pk>/', student.CertificateDeleteView.as_view(), name='certificates_delete_view'),
    # projects
    path('projects/', student.ProjectCreateAndListView.as_view(), name='project_view'),
    path('projects-update/<pk>/', student.ProjectUpdateAndDetailView.as_view(), name='project_update_detail_view'),
]
