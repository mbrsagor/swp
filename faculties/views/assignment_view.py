from django.shortcuts import redirect
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from faculties.models import Assignment, AssignmentSubmit
from faculties.forms import AssignmentForm, AssignmentSubmitForm
from faculties.filter import AssignmentFilter
from django_filters.views import FilterView


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class AssignmentListView(FilterView):
    model = Assignment
    context_object_name = 'assignments'
    template_name = 'assignment/list.html'
    filterset_class = AssignmentFilter

    def get_queryset(self):
        qs = super(AssignmentListView, self).get_queryset()
        if self.request.user.teacher:
            return qs.filter(teacher=self.request.user)
        return qs.all()


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class AssignmentCreateView(generic.CreateView):
    form_class = AssignmentForm
    template_name = 'assignment/create.html'
    success_url = reverse_lazy('faculties:assignments')

    def form_valid(self, form):
        last_date = form.cleaned_data['last_date']
        if last_date > datetime.date(datetime.now()):
            form.instance.teacher = self.request.user
            return super(AssignmentCreateView, self).form_valid(form)
        else:
            print('next date set')
            return redirect('faculties:assignments')

    def get_form_kwargs(self):
        kwargs = super(AssignmentCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class AssignmentUpdateView(generic.UpdateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'assignment/update.html'
    success_url = reverse_lazy('faculties:assignments')

    def get_form_kwargs(self):
        kwargs = super(AssignmentUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class AssignmentDeleteView(generic.DeleteView):
    model = Assignment
    success_url = reverse_lazy('faculties:assignments')

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)


# Assignment submit view
@method_decorator(user_passes_test(lambda user: user.is_superuser or user.student), name='dispatch')
class AssignmentSubmitView(LoginRequiredMixin, generic.FormView):
    form_class = AssignmentSubmitForm
    template_name = 'assignment-submit/create.html'
    get_success_url = reverse_lazy('faculties:course-schedules')

    def post(self, *args, **kwargs):
        assignment = Assignment.objects.get(pk=kwargs['pk'])
        form = self.get_form(self.form_class)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.assignment = assignment
            obj.student = self.request.user
            obj.save()
            return redirect('faculties:course-schedules-detail', pk=assignment.course_schedule.id)


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class AssignmentDetailView(generic.DetailView):
    model = Assignment
    template_name = 'assignment/detail.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class AssignmentSubmitListView(generic.ListView):
    model = AssignmentSubmit
    template_name = 'assignment-submit/list.html'







