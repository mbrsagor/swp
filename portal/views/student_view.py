from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views import generic
from portal.forms.student_form import CertificateForm, ProjectForm
from portal.models import Certificate, Project


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.student), name='dispatch')
class CertificateListView(generic.ListView):
    model = Certificate
    context_object_name = 'certificates'
    template_name = 'certificate/list.html'

    def get_queryset(self):
        qs = super(CertificateListView, self).get_queryset()
        if self.request.user.student:
            return qs.filter(student=self.request.user)
        return qs.all()


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.student), name='dispatch')
class CertificateCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = CertificateForm
    template_name = 'certificate/create.html'
    success_url = reverse_lazy('portal:certificates')
    success_message = 'The certificate created.'

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super(CertificateCreateView, self).form_valid(form)


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.student), name='dispatch')
class CertificateUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Certificate
    form_class = CertificateForm
    success_url = reverse_lazy('portal:certificates')
    template_name = 'certificate/update.html'
    success_message = 'The certificate updated.'


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.student), name='dispatch')
class CertificateDeleteView(generic.DeleteView):
    model = Certificate
    success_url = reverse_lazy('portal:certificates')

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.student), name='dispatch')
class ProjectListView(generic.ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'project/list.html'

    def get_queryset(self):
        qs = super(ProjectListView, self).get_queryset()
        if self.request.user.student:
            return qs.filter(student=self.request.user)
        return qs.all()


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.student), name='dispatch')
class ProjectCreateView(generic.CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('portal:projects')
    success_message = 'The projects created.'

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super(ProjectCreateView, self).form_valid(form)


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.student), name='dispatch')
class ProjectDetailView(generic.DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'project/detail.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.student), name='dispatch')
class ProjectUpdateView(generic.UpdateView):
    model = Project
    form_class = ProjectForm
    success_message = 'The projects updated.'
    success_url = reverse_lazy('portal:projects')
    template_name = 'project/update.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.student), name='dispatch')
class ProjectDeleteView(generic.DeleteView):
    model = Project
    success_url = reverse_lazy('portal:projects')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

