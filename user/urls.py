from django.urls import path
from user.views.user_view import RegistrationAPIView, LoginAPIView
from user.views.assessment_view import AssessmentCreateListView
from user.views.submission_view import SubmissionAPIView
from user.views.grade_view import GradeAPIView, GradeDetailView

urlpatterns = [
    path('user/registration/', RegistrationAPIView.as_view()),
    path('user/login/', LoginAPIView.as_view()),
    path('assessment/', AssessmentCreateListView.as_view()),
    path('submission/', SubmissionAPIView.as_view()),
    path('grade/', GradeAPIView.as_view()),
    path('grade/<pk>/', GradeDetailView.as_view()),
]
