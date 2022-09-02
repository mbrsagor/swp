from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.messages.views import SuccessMessageMixin
from faculties.models import Program
from faculties.forms import ProgramForm


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class ProgramCreateAndListView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Program
    form_class = ProgramForm
    context_object_name = 'programs'
    success_message = 'Program has been created.'
    success_url = '/programs/'
    template_name = 'program/list.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class ProgramUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Program
    form_class = ProgramForm
    success_message = 'Program has been updated.'
    success_url = '/programs/'
    template_name = 'program/update.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class ProgramDeleteView(generic.DeleteView):
    model = Program
    success_url = '/programs/'

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)