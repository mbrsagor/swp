from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from portal.models.notice import Notice
from portal.forms.notice import NoticeForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NoticeView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notice/notice.html'
    context_object_name = 'notice'
    success_url = '/notice/'
    success_message = 'Notice created'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NoticeDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Notice
    template_name = 'common/delete_confirm.html'
    success_url = '/notice/'
    success_message = 'Notice deleted'
