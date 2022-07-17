from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from portal.models.ebook import ReferenceEbook
from portal.forms.ebook import EbookForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EbookView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = ReferenceEbook
    form_class = EbookForm
    template_name = 'ebook/ebook.html'
    context_object_name = 'ebook'
    success_url = '/ebook/'
    success_message = 'Ebook Added'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EbookDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = ReferenceEbook
    template_name = 'common/delete_confirm.html'
    success_url = '/ebook/'
    success_message = 'E-book deleted'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EbookDownloadView(generic.ListView):
    model = ReferenceEbook
    template_name = 'ebook/download.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['ebook'] = ReferenceEbook.objects.all()
        print(ctx)
        return ctx
