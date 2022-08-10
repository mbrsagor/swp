from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from portal.models import Mark
from portal.forms.mark_form import MarkForm


class MarkListView(LoginRequiredMixin, generic.CreateView,  generic.ListView):
    model = Mark
    form_class = MarkForm
    context_object_name = 'marks'
    success_url = '/marks/'
    template_name = 'mark/marks.html'
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(MarkListView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class MarkUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Mark
    form_class = MarkForm
    success_url = '/marks/'
    template_name = 'mark/update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
