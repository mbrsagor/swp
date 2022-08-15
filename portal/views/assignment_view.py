from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from portal.models import Assignment, Mark
from portal.forms.assignment_form import AssignmentForm
from users.models import TeacherProfile


class AssignmentCreateAndListView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Assignment
    form_class = AssignmentForm
    context_object_name = 'assignments'
    success_url = '/assignments/'
    success_message = 'Successfully created assignment.'
    template_name = 'assignment/list.html'

    def get_queryset(self):
        if self.request.user.roll == 'STUDENT':
            return self.model.objects.filter(student=self.request.user)
        elif self.request.user.roll == 'TEACHER':
            profile = TeacherProfile.objects.get(user=self.request.user)
            subjects = [x.id for x in profile.subject.all()]
            return self.model.objects.filter(subject__in=subjects)
        else:
            return self.model.objects.all()

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.student = self.request.user
        return super(AssignmentCreateAndListView, self).form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AssignmentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Assignment
    form_class = AssignmentForm
    success_url = '/assignments/'
    template_name = 'assignment/update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class AssignmentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Assignment
    template_name = 'assignment/update.html'


class AssignmentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Assignment
    success_url = '/assignments/'

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)
