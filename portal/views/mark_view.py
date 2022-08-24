from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views import generic
from django.urls import reverse_lazy
from portal.models import Mark
from portal.forms.mark_form import MarkForm


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class MarkListView(generic.CreateView,  generic.ListView):
    model = Mark
    form_class = MarkForm
    context_object_name = 'marks'
    success_url = reverse_lazy('portal:marks')
    template_name = 'mark/list.html'
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(MarkListView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class MarkUpdateView(generic.UpdateView):
    model = Mark
    form_class = MarkForm
    success_url = reverse_lazy('portal:marks')
    template_name = 'mark/update.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class MarkDeleteView(generic.DeleteView):
    model = Mark
    success_url = reverse_lazy('portal:marks')

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)
