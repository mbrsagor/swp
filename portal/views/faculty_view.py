from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.messages.views import SuccessMessageMixin
from portal.models import Faculty, Department, Semester
from portal.forms.faculty_form import FacultyForm, DepartmentForm, SemesterForm


# faculty views start
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
# end faculty views


# Start Department view
@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class DepartmentCreateAndListView(SuccessMessageMixin, generic.CreateView,  generic.ListView):
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
# end Department view


# start semester view
@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class SemesterCreateAndListView(SuccessMessageMixin, generic.CreateView,  generic.ListView):
    model = Semester
    form_class = SemesterForm
    template_name = 'semester/list.html'
    context_object_name = 'semesters'
    success_url = '/semesters/'
    success_message = 'Semester created'


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
# end semester view
