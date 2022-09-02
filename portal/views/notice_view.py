from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from portal.models import Notice
from portal.forms.notice_form import NoticeForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class NoticeListView(generic.ListView):
    model = Notice
    context_object_name = 'notices'
    template_name = 'notice/list.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class NoticeCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = NoticeForm
    success_url = reverse_lazy('portal:notices')
    success_message = 'Notice successfully created'
    template_name = 'notice/create.html'

    def form_valid(self, form):
        form.instance.admin = self.request.user
        return super(NoticeCreateView, self).form_valid(form)


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class NoticeUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Notice
    form_class = NoticeForm
    template_name = 'notice/update.html'
    success_url = reverse_lazy('portal:notices')
    success_message = 'Notice successfully created'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class NoticeDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Notice
    template_name = 'common/delete_confirm.html'
    success_url = reverse_lazy('portal:notices')
    success_message = 'Notice successfully deleted'
