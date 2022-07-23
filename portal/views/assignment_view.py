from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from portal.models.assinment import Assignment
from portal.forms.assignment_form import AssignmentForm, ReportForm, MarkForm


class AssignmentCreateAndListView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Assignment
    form_class = AssignmentForm
    context_object_name = 'assignments'
    success_url = '/assignments/'
    success_message = 'Successfully created assignment.'
    template_name = 'assignment/assignment.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.teacher = self.request.user
        instance.save()
        form.save_m2m()
        return super(AssignmentCreateAndListView, self).form_valid(form)


class AssignmentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Assignment
    template_name = 'assignment/detail.html'


class AssignmentMarkView(generic.View):

    def get(self, *args, **kwargs):
        assignment = Assignment.objects.get(pk=kwargs['pk'])
        form = MarkForm()
        title = 'Assignment Mark Submit'
        context = {
            'title': title,
            'form': form,
            'assignment': assignment
        }
        return render(self.request, 'assignment/mark-create.html', context)

    def post(self, *args, **kwargs):
        form = MarkForm(self.request.POST)
        assignment = Assignment.objects.get(pk=kwargs['pk'])
        if form.is_valid():
            instance = form.save(commit=False)
            instance.teacher = self.request.user
            instance.assignment = assignment
            instance.save()
            return redirect('assignment_create_and_list_view')


class AssignmentReport(generic.View):

    def get(self, *args, **kwargs):
        assignment = Assignment.objects.get(pk=kwargs['pk'])
        form = ReportForm()
        title = 'Assignment Report Submit'
        context = {
            'title': title,
            'form': form,
            'assignment': assignment
        }
        return render(self.request, 'assignment/report-create.html', context)

    def post(self, *args, **kwargs):
        form = ReportForm(self.request.POST)
        assignment = Assignment.objects.get(pk=kwargs['pk'])
        if form.is_valid():
            instance = form.save(commit=False)
            instance.teacher = self.request.user
            instance.assignment = assignment
            instance.save()
            return redirect('assignment_create_and_list_view')
