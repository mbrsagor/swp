from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms.student import CertificateForm, ProjectForm
from ..models.student import Certificate, Project


class CertificateListAndCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Certificate
    form_class = CertificateForm
    context_object_name = 'certificates'
    template_name = 'certificate/certificate.html'
    success_url = '/certificates/'
    success_message = 'The certificate created.'

    def form_valid(self, form):
        student = Certificate.objects.filter(student=self.request.user)

        if student.exists():
            next_url = self.request.META['HTTP_REFERER']
            messages.error(self.request, 'Already added your certificate.')
            return HttpResponseRedirect(next_url)

        if not student.exists():
            form.instance.student = self.request.user
            form.save()
            return super(CertificateListAndCreateView, self).form_valid(form)


class CertificateDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Certificate
    success_url = '/certificates/'
    success_message = 'The certificate Deleted.'
    template_name = 'common/delete_confirm.html'


class CertificateUpdateAndDetailView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView, generic.DetailView):
    model = Certificate
    form_class = CertificateForm
    context_object_name = 'certificate'
    template_name = 'certificate/detail.html'
    success_message = 'The certificate updated.'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('certificate_detail_update_view', kwargs={'pk': pk})


class ProjectCreateAndListView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    model = Project
    form_class = ProjectForm
    context_object_name = 'projects'
    template_name = 'project/project.html'
    success_url = '/projects/'
    success_message = 'The projects created.'


class ProjectUpdateAndDetailView(LoginRequiredMixin, generic.UpdateView, generic.DetailView):
    model = Project
    form_class = ProjectForm
    context_object_name = 'project'
    template_name = 'project/detail.html'
    success_message = 'The projects updated.'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("project_update_detail_view", kwargs={"pk": pk})
