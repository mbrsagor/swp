from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from portal.forms.student_form import CertificateForm, ProjectForm
from portal.models import Certificate, Project


class CertificateListView(LoginRequiredMixin, generic.ListView):
    model = Certificate
    context_object_name = 'certificates'
    template_name = 'certificate/certificate.html'

    def get_queryset(self):
        if self.request.user.roll == 'STUDENT':
            return super(CertificateListView, self).get_queryset().filter(student=self.request.user)
        return super(CertificateListView, self).get_queryset()


class CertificateCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CertificateForm
    template_name = 'certificate/create.html'
    success_url = '/certificates/'
    success_message = 'The certificate created.'

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super(CertificateCreateView, self).form_valid(form)


class CertificateUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Certificate
    form_class = CertificateForm
    success_url = '/certificates/'
    template_name = 'certificate/update.html'
    success_message = 'The certificate updated.'


class CertificateDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Certificate
    success_url = '/certificates/'

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project/list.html'

    def get_queryset(self):
        if self.request.user.roll == 'STUDENT':
            return super(ProjectListView, self).get_queryset().filter(student=self.request.user)
        return super(ProjectListView, self).get_queryset()


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/create.html'
    success_url = '/projects/'
    success_message = 'The projects created.'

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super(ProjectCreateView, self).form_valid(form)


class ProjectUpdateAndDetailView(LoginRequiredMixin, generic.UpdateView, generic.DetailView):
    model = Project
    form_class = ProjectForm
    context_object_name = 'project'
    template_name = 'project/detail.html'
    success_message = 'The projects updated.'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("project_update_detail_view", kwargs={"pk": pk})


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = '/projects/'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

