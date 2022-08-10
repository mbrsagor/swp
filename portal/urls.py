from django.urls import path
from portal.views import student_view
from portal.views import ebook
from portal.views import subject_view
from portal.views import assignment_view
from portal.views import routine
from portal.views import notice
from portal.views import mark
from portal.views import faculty_view

urlpatterns = [
    # faculty
    path('faculties/', faculty_view.FacultyCreateAndListView.as_view(), name='faculties-create-listview'),
    path('faculties/update/<pk>/', faculty_view.FacultyUpdateView.as_view(), name='faculties-update-view'),
    path('faculties/delete/<pk>/', faculty_view.FacultyDeleteView.as_view(), name='faculties-delete-view'),
    # Department
    path('departments/', faculty_view.DepartmentCreateAndListView.as_view(), name='departments-create-listview'),
    path('departments/update/<pk>/', faculty_view.DepartmentUpdateView.as_view(),
         name='departments-update-view'),
    path('departments/delete/<pk>/', faculty_view.DepartmentDeleteView.as_view(),
         name='departments-delete-view'),
    # Semester
    path('semesters/', faculty_view.SemesterCreateAndListView.as_view(), name='semesters-create-listview'),
    path('semesters/update/<pk>/', faculty_view.SemesterUpdateView.as_view(), name='semesters-update-view'),
    path('semesters/delete/<pk>/', faculty_view.SemesterDeleteView.as_view(), name='semesters-delete-view'),
    # Subject
    path('subjects/', subject_view.SubjectCreateListView.as_view(), name="subject_create_listview"),
    path('subjects/update/<pk>/', subject_view.SubjectUpdateView.as_view(), name="subject_update_view"),
    path('subjects/delete/<pk>/', subject_view.SubjectDeleteView.as_view(), name="subject_delete"),
    path('subjects/enroll/', subject_view.SubjectEnrollCreateAndListView.as_view(), name="subject_enroll"),
    path('subjects/enroll/update/<pk>/', subject_view.SubjectEnrollUpdateView.as_view(), name='subjects_enroll_update_view'),
    path('subjects/enroll/approve/<pk>/', subject_view.EnrollApproveView.as_view(), name='subjects_enroll_approve_view'),
    path('subjects/enroll/delete/<pk>/', subject_view.SubjectEnrollDeleteView.as_view(), name="subject_enroll_delete_view"),
    # certificate urls
    path('certificates/', student_view.CertificateListView.as_view(), name='certificates_view'),
    path('certificate/create/', student_view.CertificateCreateView.as_view(), name='certificate_create_view'),
    path('certificate/update/<pk>/', student_view.CertificateUpdateView.as_view(), name='certificate_update_view'),
    path('certificates/delete/<pk>/', student_view.CertificateDeleteView.as_view(), name='certificates_delete_view'),
    # projects
    path('projects/', student_view.ProjectListView.as_view(), name='project_view'),
    path('projects/create/', student_view.ProjectCreateView.as_view(), name='project_create_view'),
    path('projects/update/<pk>/', student_view.ProjectUpdateAndDetailView.as_view(),
         name='project_update_detail_view'),
    path('projects/delete/<pk>/', student_view.ProjectDeleteView.as_view(), name='project_delete_view'),
    # assignments
    path('assignments/', assignment_view.AssignmentCreateAndListView.as_view(),
         name='assignment_create_and_list_view'),
    path('assignments/update/<pk>/', assignment_view.AssignmentUpdateView.as_view(),
         name='assignment_update_view'),
    path('assignments/delete/<pk>/', assignment_view.AssignmentDeleteView.as_view(),
         name='assignment_delete_view'),
    path('assignments/<pk>/', assignment_view.AssignmentDetailView.as_view(),
         name='assignment_detail_view'),
    # mark
    path('marks/', mark.MarkListView.as_view(), name='marks_view'),
    path('marks/update/<pk>/', mark.MarkUpdateView.as_view(), name='marks_update_view'),
    # E-Books urls
    path('books/', ebook.BooksListView.as_view(), name='books_list_view'),
    path('books/detail/<pk>/', ebook.BookDetailView.as_view(), name='books_detail_view'),
    path('books/create/', ebook.BookCreateView.as_view(), name='books_create_view'),
    path('books/update/<pk>/', ebook.BookUpdateView.as_view(), name='books_update_view'),
    # notice
    path('notices/', notice.NoticeListView.as_view(), name='notices-view'),
    path('notices/create/', notice.NoticeCreateView.as_view(), name='notices-create-view'),
    path('notices/update/<pk>/', notice.NoticeUpdateView.as_view(), name='notices-update-view'),
    path('notices/delete/<pk>/', notice.NoticeDeleteView.as_view(), name='notice-delete-view'),
    # routine
    path('routines/', routine.RoutineCreateAndListView.as_view(), name='routines_view'),
    path('routines/update/<pk>/', routine.RoutineUpdateView.as_view(), name='routines_update_view'),
    path('routines/delete/<pk>/', routine.RoutineDeleteView.as_view(), name='routine_delete_view'),
]
