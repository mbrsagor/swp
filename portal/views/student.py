from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from ..forms.student import CertificateForm, ProjectForm
from ..models.student import Certificate, Project


class CertificateListView(LoginRequiredMixin, generic.ListView):
    model = Certificate
    context_object_name = 'certificates'
    template_name = 'certificate/certificate.html'

    def get_context_data(self, **kwargs):
        context = super(CertificateListView, self).get_context_data(**kwargs)
        context['created_certificate'] = Certificate.objects.filter(student=self.request.user)
        return context


class CertificateCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Certificate
    form_class = CertificateForm
    template_name = 'certificate/create.html'
    success_url = '/certificates/'
    success_message = 'The certificate created.'
    error_message = 'Already added your certificate.'

    def form_valid(self, form):
        student = Certificate.objects.filter(student=self.request.user)

        if student.exists():
            next_url = self.request.META['HTTP_REFERER']
            messages.error(self.request, self.error_message)
            print(self.error_message)
            return HttpResponseRedirect(next_url)
        instance = form.save(commit=False)
        instance.student = self.request.user
        instance.save()
        return super(CertificateCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs = super(CertificateCreateView, self).get_context_data(**kwargs)
        kwargs['title'] = 'Created Certificate'
        return kwargs


class CertificateUpdateAndDetailView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView, generic.DetailView):
    model = Certificate
    form_class = CertificateForm
    context_object_name = 'certificate'
    template_name = 'certificate/detail.html'
    success_message = 'The certificate updated.'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('certificate_detail_update_view', kwargs={'pk': pk})


class CertificateDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Certificate
    success_url = '/certificates/'

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)


class ProjectCreateAndListView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    model = Project
    form_class = ProjectForm
    context_object_name = 'projects'
    template_name = 'project/project.html'
    success_url = '/projects/'
    success_message = 'The projects created.'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.student = self.request.user
        instance.save()
        return super().form_valid(form)


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

