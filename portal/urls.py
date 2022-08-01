from django.urls import path
from portal.views import student
from portal.views import ebook
from portal.views import subject
from portal.views import section
from portal.views import assignment_view
from portal.views import routine
from portal.views import notice
from portal.views import mark

urlpatterns = [
    # Subject
    path('subjects/', subject.SubjectCreateListView.as_view(), name="subject_create_listview"),
    path('subjects/update/<pk>/', subject.SubjectUpdateView.as_view(), name="subject_update_view"),
    path('subjects/delete/<pk>/', subject.SubjectDeleteView.as_view(), name="subject_delete"),
    path('subjects/enroll/', subject.SubjectEnrollCreateAndListView.as_view(), name="subject_enroll"),
    path('subjects/enroll/update/<pk>/', subject.SubjectEnrollUpdateView.as_view(), name='subjects_enroll_update_view'),
    path('subjects/enroll/approve/<pk>/', subject.EnrollApproveView.as_view(), name='subjects_enroll_approve_view'),
    path('subjects/enroll/delete/<pk>/', subject.SubjectEnrollDeleteView.as_view(), name="subject_enroll_delete_view"),
    # section urls
    path('section/', section.SectionView.as_view(), name='section_view'),
    path('section/delete/<pk>/', section.SectionDeleteView.as_view(), name='section_delete_view'),
    # certificate urls
    path('certificates/', student.CertificateListView.as_view(), name='certificates_view'),
    path('certificate/create/', student.CertificateCreateView.as_view(), name='certificate_create_view'),
    path('certificate-detail/<pk>/', student.CertificateUpdateAndDetailView.as_view(),
         name='certificate_detail_update_view'),
    path('certificates/delete/<pk>/', student.CertificateDeleteView.as_view(), name='certificates_delete_view'),
    # projects
    path('projects/', student.ProjectCreateAndListView.as_view(), name='project_view'),
    path('projects/update/<pk>/', student.ProjectUpdateAndDetailView.as_view(),
         name='project_update_detail_view'),
    path('projects/delete/<pk>/', student.ProjectDeleteView.as_view(), name='project_delete_view'),
    # assignments
    path('assignments/', assignment_view.AssignmentCreateAndListView.as_view(),
         name='assignment_create_and_list_view'),
    path('assignments/<pk>/', assignment_view.AssignmentDetailView.as_view(),
         name='assignment_detail_view'),
    path('assignments/reports/<pk>/', assignment_view.AssignmentReportView.as_view(),
         name='assignment_reports_view'),
    path('assignments/marks/<pk>/', assignment_view.AssignmentMarkView.as_view(),
         name='assignment_marks_view'),
    # mark
    path('marks/', mark.MarkListView.as_view(), name='marks_view'),
    path('marks/add/<pk>/', mark.MarkAddView.as_view(), name='marks_add_view'),
    path('marks/update/<pk>/', mark.MarkUpdateView.as_view(), name='marks_update_view'),
    # E-Books urls
    path('books/', ebook.BooksListView.as_view(), name='books_list_view'),
    path('books/create/', ebook.BookCreateView.as_view(), name='books_create_view'),
    path('books/update/<pk>/', ebook.BookUpdateView.as_view(), name='books_update_view'),
    # notice
    path('notices/', notice.NoticeCreateAndListView.as_view(), name='notices_view'),
    path('notices/delete/<pk>/', notice.NoticeDeleteView.as_view(), name='notice_delete_view'),
    # routine
    path('routines/', routine.RoutineCreateAndListView.as_view(), name='routines_view'),
    path('routines/delete/<pk>/', routine.RoutineDeleteView.as_view(), name='routine_delete_view'),
]
