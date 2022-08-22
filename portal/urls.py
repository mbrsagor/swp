from django.urls import path
from portal.views import student_view
from portal.views import ebook_view
from portal.views import routine
from portal.views import notice_view
from portal.views import mark


app_name = 'portal'
urlpatterns = [
    # certificate urls
    path('certificates/', student_view.CertificateListView.as_view(), name='certificates'),
    path('certificates/create/', student_view.CertificateCreateView.as_view(), name='certificates-create'),
    path('certificates/<pk>/update/', student_view.CertificateUpdateView.as_view(), name='certificates-update'),
    path('certificates/<pk>/delete/', student_view.CertificateDeleteView.as_view(), name='certificates-delete'),
    # projects
    path('projects/', student_view.ProjectListView.as_view(), name='projects'),
    path('projects/create/', student_view.ProjectCreateView.as_view(), name='projects-create'),
    path('projects/<pk>/detail/', student_view.ProjectDetailView.as_view(), name='projects-detail'),
    path('projects/<pk>/update/', student_view.ProjectUpdateView.as_view(),
         name='projects-update'),
    path('projects/<pk>/delete/', student_view.ProjectDeleteView.as_view(), name='projects-delete'),
    # mark
    path('marks/', mark.MarkListView.as_view(), name='marks'),
    path('marks/<pk>/update/', mark.MarkUpdateView.as_view(), name='marks-update'),
    path('marks/<pk>/delete/', mark.MarkDeleteView.as_view(), name='marks-delete'),

    # E-Books urls
    path('books/', ebook_view.BooksListView.as_view(), name='books'),
    path('books/create/', ebook_view.BookCreateView.as_view(), name='books-create'),
    path('books/<pk>/detail/', ebook_view.BookDetailView.as_view(), name='books-detail'),
    path('books/<pk>/update', ebook_view.BookUpdateView.as_view(), name='books-update'),
    path('books/<pk>/delete', ebook_view.BookDeleteView.as_view(), name='books-delete'),
    # notice
    path('notices/', notice_view.NoticeListView.as_view(), name='notices'),
    path('notices/create/', notice_view.NoticeCreateView.as_view(), name='notices-create'),
    path('notices/<pk>/update/', notice_view.NoticeUpdateView.as_view(), name='notices-update'),
    path('notices/<pk>/delete/', notice_view.NoticeDeleteView.as_view(), name='notice-delete'),
    # routine
    path('routines/', routine.RoutineCreateAndListView.as_view(), name='routines'),
    path('routines/<pk>/update', routine.RoutineUpdateView.as_view(), name='routines-update'),
    path('routines/<pk>/delete', routine.RoutineDeleteView.as_view(), name='routines-delete'),
]
