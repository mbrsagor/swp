from django.http import HttpResponseRedirect
from .views import *
from ..forms import CertificateForm
from django.contrib import messages


class CertificateListAndCreateView(SuccessMessageMixin, generic.CreateView, generic.ListView):
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


class CertificateDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Certificate
    success_url = '/certificates/'
    success_message = 'The certificate Deleted.'
    template_name = 'common/delete_confirm.html'
