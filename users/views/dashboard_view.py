from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import StudentProfile, TeacherProfile
from faculties.models import CourseSchedule, Assignment, AssignmentSubmit


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        if self.request.user.student:
            context['profile'] = StudentProfile.objects.get(user=self.request.user)
            context['assignment_submit'] = AssignmentSubmit.objects.filter(student=self.request.user)
            context['course_schedule'] = CourseSchedule.objects.filter(students=self.request.user)
            return context

        if self.request.user.teacher:
            context['profile'] = TeacherProfile.objects.get(user=self.request.user)
            context['course_schedule'] = CourseSchedule.objects.filter(teacher=self.request.user)
            context['assignments'] = Assignment.objects.filter(teacher=self.request.user)
            return context


