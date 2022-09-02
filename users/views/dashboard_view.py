from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from faculties.models import CourseSchedule, Assignment, AssignmentSubmit
from faculties.models import Faculty, Department


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        if self.request.user.student:
            context['assignment_submit'] = AssignmentSubmit.objects.filter(student=self.request.user)
            context['course_schedule'] = CourseSchedule.objects.filter(students=self.request.user)
        elif self.request.user.teacher:
            context['course_schedule'] = CourseSchedule.objects.filter(teacher=self.request.user)
            context['assignments'] = Assignment.objects.filter(teacher=self.request.user)
        else:
            context['faculties'] = Faculty.objects.all()
            context['departments'] = Department.objects.all()
        return context



