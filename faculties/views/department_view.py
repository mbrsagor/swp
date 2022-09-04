from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.messages.views import SuccessMessageMixin
from faculties.models import Department
from faculties.forms import DepartmentForm


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class DepartmentCreateAndListView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Department
    form_class = DepartmentForm
    template_name = 'department/list.html'
    context_object_name = 'departments'
    success_url = '/departments/'
    success_message = 'Department created'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class DepartmentUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'department/update.html'
    success_url = '/departments/'
    success_message = 'Department updated'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class DepartmentDeleteView(generic.DeleteView):
    model = Department
    form_class = DepartmentForm
    success_url = '/departments/'

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
