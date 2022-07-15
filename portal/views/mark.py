from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models.assinment import Mark
from ..forms.assignment import MarkForm


class MarkCreateAdnListView(LoginRequiredMixin, generic.CreateView, generic.ListView):
    model = Mark
    form_class = MarkForm
    context_object_name = 'marks'
    success_url = '/marks/'
    template_name = 'mark/marks.html'
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(MarkCreateAdnListView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs = super(MarkCreateAdnListView, self).get_context_data(**kwargs)
        kwargs['title'] = 'Assignment Create'
        return kwargs


class MarkUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Mark
    form_class = MarkForm
    success_url = '/marks/'
    template_name = 'mark/update.html'

    def get_context_data(self, **kwargs):
        kwargs = super(MarkUpdateView, self).get_context_data(**kwargs)
        kwargs['title'] = 'Marks Update'
        return kwargs
