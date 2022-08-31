from django.db.models import Q
from django.core import serializers
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.urls import reverse_lazy
from portal.models import Mark
from portal.forms.mark_form import MarkForm, MarkUpdateForm
from users.models import StudentProfile
from faculties.models import CourseSchedule


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class MarkListView(generic.CreateView,  generic.ListView):
    model = Mark
    form_class = MarkForm
    success_url = reverse_lazy('portal:marks')
    template_name = 'mark/list.html'

    def get_context_data(self, **kwargs):
        context = super(MarkListView, self).get_context_data(**kwargs)
        course_schedule = CourseSchedule.objects.filter(teacher=self.request.user)
        course_schedules_data = serializers.serialize('json', course_schedule, fields={'course', 'students'}, use_natural_foreign_keys=True, use_natural_primary_keys=True)
        context["course_schedules"] = course_schedules_data
        return context

    def get_queryset(self):
        qs = super(MarkListView, self).get_queryset()
        if self.request.user.teacher:
            return qs.filter(teacher=self.request.user)
        else:
            return qs.all()
    
    def form_valid(self, form):
        course = form.cleaned_data['course_schedule']
        student = form.cleaned_data['student']
        status = form.cleaned_data['status']

        course_schedule = CourseSchedule.objects.get(course__title=course)
        if Mark.objects.filter(course_schedule=course_schedule, student__username=student, status=status).exists():
            return redirect('portal:marks')
        form.instance.teacher = self.request.user
        return super(MarkListView, self).form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(MarkListView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class MarkUpdateView(generic.UpdateView):
    model = Mark
    form_class = MarkUpdateForm
    success_url = reverse_lazy('portal:marks')
    template_name = 'mark/update.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class MarkDeleteView(generic.DeleteView):
    model = Mark
    success_url = reverse_lazy('portal:marks')

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class MarkSearchView(generic.ListView):
    model = Mark
    template_name = 'mark/search.html'

    def get_queryset(self):
        try:
            if not (query := self.request.GET.get("q")):
                return self.model.objects.none()
            if self.request.user.teacher:
                profile = StudentProfile.objects.get(unique_id__icontains=query)
                return self.model.objects.filter(
                    (Q(student__username__icontains=profile.user.username) & Q(teacher=self.request.user)))
            else:
                profile = StudentProfile.objects.get(unique_id__icontains=query)
                return self.model.objects.filter(Q(student__username__icontains=profile.user.username))
        except:
            return self.model.objects.none()
