from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from portal.models.assinment import Assignment
from portal.forms.assignment_form import AssignmentForm, ReportForm, MarkForm


class AssignmentCreateAndListView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Assignment
    form_class = AssignmentForm
    context_object_name = 'assignments'
    success_url = '/assignments/'
    success_message = 'Successfully created assignment.'
    template_name = 'assignment/assignment.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.student = self.request.user
        return super(AssignmentCreateAndListView, self).form_valid(form)


class AssignmentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Assignment
    template_name = 'assignment/detail.html'

class MarkListView(LoginRequiredMixin, generic.ListView):
    model = Mark
    template_name = 'mark/list.html'


class AssignmentMarkView(LoginRequiredMixin, generic.View):

    template_name = 'assignment/mark-create.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MarkForm()
        return context

    def post(self, *args, **kwargs):
        form = MarkForm(self.request.POST)
        assignment = Assignment.objects.get(pk=kwargs['pk'])
        if form.is_valid():
            instance = form.save(commit=False)
            instance.teacher = self.request.user
            instance.assignment = assignment
            instance.save()
            return redirect('assignment_create_and_list_view')


class AssignmentReportView(LoginRequiredMixin, generic.TemplateView):

    template_name = 'assignment/report-create.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReportForm()
        return context

    def post(self, *args, **kwargs):
        form = ReportForm(self.request.POST)
        assignment = Assignment.objects.get(pk=kwargs['pk'])
        if form.is_valid():
            instance = form.save(commit=False)
            instance.teacher = self.request.user
            instance.assignment = assignment
            instance.save()
            return redirect('assignment_create_and_list_view')
