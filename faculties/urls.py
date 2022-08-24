from django.urls import path
from faculties.views import (
    course_view,
    department_view,
    faculty_view,
    program_view,
    semester_view,
    assignment_view,
)

app_name = 'faculties'
urlpatterns = [
    # faculty url config
    path('faculties/', faculty_view.FacultyCreateAndListView.as_view(), name='faculties'),
    path('faculties/<pk>/update/', faculty_view.FacultyUpdateView.as_view(), name='faculties-update'),
    path('faculties/<pk>/delete/', faculty_view.FacultyDeleteView.as_view(), name='faculties-delete'),
    # Department url config
    path('departments/', department_view.DepartmentCreateAndListView.as_view(), name='departments'),
    path('departments/<pk>/update/', department_view.DepartmentUpdateView.as_view(),
         name='departments-update'),
    path('departments/delete/<pk>/', department_view.DepartmentDeleteView.as_view(),
         name='departments-delete'),
    # programs url config
    path('programs/', program_view.ProgramCreateAndListView.as_view(), name='programs'),
    path('programs/<pk>/create/', program_view.ProgramUpdateView.as_view(), name='programs-update'),
    path('programs/<pk>/delete/', program_view.ProgramDeleteView.as_view(), name='programs-delete'),
    # Semester url config
    path('semesters/', semester_view.SemesterListView.as_view(), name='semesters'),
    path('semesters/create/', semester_view.SemesterCreateView.as_view(), name='semesters-create'),
    path('semesters/<pk>/update/', semester_view.SemesterUpdateView.as_view(), name='semesters-update'),
    path('semesters/<pk>/delete/', semester_view.SemesterDeleteView.as_view(), name='semesters-delete'),
    # course url config
    path('courses/', course_view.CourseCreateListView.as_view(), name="courses"),
    path('courses/<pk>/detail/', course_view.CourseDetailView.as_view(), name="courses-detail"),
    path('courses/<pk>/update/', course_view.CourseUpdateView.as_view(), name="courses-update"),
    path('courses/<pk>/delete/', course_view.CourseDeleteView.as_view(), name="courses-delete"),
    # course schedule url config
    path('course-schedules/', course_view.CourseScheduleListView.as_view(), name="course-schedules"),
    path('course-schedules/<pk>/detail', course_view.CourseScheduleDetailView.as_view(), name="course-schedules-detail"),
    path('course-schedules/create/', course_view.CourseScheduleCreateView.as_view(), name="course-schedules-create"),
    path('course-schedules/<pk>/join/', course_view.CourseScheduleEnrollView.as_view(), name="course-schedules-join"),
    path('course-schedules/<pk>/update/', course_view.CourseScheduleUpdateView.as_view(),
         name="course-schedules-update"),
    path('course-schedules/<pk>/delete/', course_view.CourseScheduleDeleteView.as_view(),
         name="course-schedules-delete"),
    path('course-schedules/enroll/', course_view.CourseScheduleView.as_view(),
         name="course-schedules-enroll"),
    # assignment url config
    path('assignments/', assignment_view.AssignmentListView.as_view(), name='assignments'),
    path('assignments/create/', assignment_view.AssignmentCreateView.as_view(), name='assignments-create'),
    path('assignments/<pk>/update/', assignment_view.AssignmentUpdateView.as_view(), name='assignments-update'),
    path('assignments/<pk>/delete/', assignment_view.AssignmentDeleteView.as_view(), name='assignments-delete'),
    # assignment submit url
    path('assignment-submits/<pk>/create/', assignment_view.AssignmentSubmitView.as_view(),
         name='assignment-submits-create'),
]
