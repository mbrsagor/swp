from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views import generic, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from faculties.models import Course, CourseSchedule
from faculties.forms import CourseForm, CourseScheduleForm
from users.models import StudentProfile
from django.db.models import Q
from django.conf import settings


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class CourseCreateListView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Course
    form_class = CourseForm
    success_url = reverse_lazy('faculties:courses')
    context_object_name = 'courses'
    success_message = 'The Course has been created.'
    template_name = 'course/list.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class CourseUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Course
    form_class = CourseForm
    success_message = 'The Course has been updated.'
    success_url = reverse_lazy('faculties:courses')
    template_name = 'course/update.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'course/detail.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class CourseDeleteView(generic.DeleteView):
    model = Course
    success_url = reverse_lazy('faculties:courses')

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class CourseScheduleListView(LoginRequiredMixin, generic.ListView):
    model = CourseSchedule
    template_name = 'course-schedule/list.html'

    def get_queryset(self, *args, **kwargs):
        qs = super(CourseScheduleListView, self).get_queryset()

        if self.request.user.teacher:
            return qs.filter(teacher=self.request.user)
        return qs.all()


class CourseScheduleDetailView(LoginRequiredMixin, generic.DetailView):
    model = CourseSchedule
    template_name = 'course-schedule/detail.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class CourseScheduleCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = CourseScheduleForm
    template_name = 'course-schedule/create.html'
    success_url = reverse_lazy('faculties:course-schedules')
    success_message = 'Course Schedule Create'

    def form_valid(self, form):
        teacher = form.cleaned_data['teacher']
        course = form.cleaned_data['course']
        course_schedule = CourseSchedule.objects.filter(teacher=teacher, course=course)
        if not course_schedule:
            print('save the course schedule')
            return super(CourseScheduleCreateView, self).form_valid(form)
        print('already teacher exists the course schedule.')
        return redirect('faculties:course-schedules')


@method_decorator(user_passes_test(lambda user: user.student), name='dispatch')
class CourseScheduleView(generic.ListView):
    model = CourseSchedule
    template_name = 'course-schedule/course-enroll.html'

    def get_queryset(self):
        return CourseSchedule.objects.filter(~Q(students=self.request.user))


@method_decorator(user_passes_test(lambda user: user.student), name='dispatch')
class CourseScheduleEnrollView(View):
    def get(self, *args, **kwargs):
        # print(kwargs['pk'])
        course_schedule = CourseSchedule.objects.get(pk=kwargs['pk'])
        if CourseSchedule.objects.filter(students=self.request.user, course=course_schedule.course).exists():
            messages.info(self.request, 'Already Joined')
            return HttpResponseRedirect(self.request.META['HTTP_REFERER'])
        profile = StudentProfile.objects.get(user=self.request.user)

        if profile.credit >= settings.MAX_CREDIT:
            messages.info(self.request, 'Your Credit Completed.')
            return HttpResponseRedirect(self.request.META['HTTP_REFERER'])
        course_schedule = CourseSchedule.objects.get(pk=kwargs['pk'])
        profile.credit += course_schedule.course.credit
        profile.save()
        course_schedule.students.add(self.request.user)
        messages.info(self.request, 'Successfully Joined')
        return HttpResponseRedirect(self.request.META['HTTP_REFERER'])


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class CourseScheduleUpdateView(generic.UpdateView):
    model = CourseSchedule
    form_class = CourseScheduleForm
    success_url = reverse_lazy('faculties:course-schedules')
    template_name = 'course-schedule/update.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class CourseScheduleDeleteView(generic.DeleteView):
    model = CourseSchedule
    success_url = reverse_lazy('faculties:course-schedules')

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)
