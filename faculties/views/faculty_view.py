from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.messages.views import SuccessMessageMixin
from faculties.models import Faculty
from faculties.forms import FacultyForm


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class FacultyCreateAndListView(SuccessMessageMixin, generic.CreateView,  generic.ListView):
    model = Faculty
    form_class = FacultyForm
    template_name = 'faculty/list.html'
    context_object_name = 'faculties'
    success_url = '/faculties/'
    success_message = 'Faculty created'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class FacultyUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Faculty
    form_class = FacultyForm
    template_name = 'faculty/update.html'
    success_url = '/faculties/'
    success_message = 'Faculty updated'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class FacultyDeleteView(generic.DeleteView):
    model = Faculty
    success_url = '/faculties/'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)