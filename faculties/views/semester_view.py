from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from faculties.models import Semester
from faculties.forms import SemesterForm


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class SemesterListView(SuccessMessageMixin, generic.ListView):
    model = Semester
    context_object_name = 'semesters'
    template_name = 'semester/list.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class SemesterCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = SemesterForm
    success_url = reverse_lazy('faculties:semesters')
    success_message = 'Semester created'
    template_name = 'semester/create.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class SemesterUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Semester
    form_class = SemesterForm
    template_name = 'semester/update.html'
    success_url = '/semesters/'
    success_message = 'Semester updated'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class SemesterDeleteView(generic.DeleteView):
    model = Semester
    form_class = SemesterForm
    success_url = '/semesters/'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
