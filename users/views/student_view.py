import json
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from users.models import User, Student, StudentProfile
from users.forms.student_form import StudentSingUpForm, StudentProfileForm, StudentForm
from faculties.models import Faculty, Department, Program
from faculties.models import CourseSchedule


class RegistrationView(SuccessMessageMixin, generic.CreateView):
    form_class = StudentSingUpForm
    success_url = reverse_lazy("users:login")
    success_message = "Successfully registration done."
    template_name = "auth/register.html"

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        faculties = Faculty.objects.all().order_by("name")
        faculty_list = list(faculties.values("name", "id"))
        context["faculties"] = json.dumps(faculty_list)
        departments = Department.objects.all().order_by("name")
        faculty_list = list(departments.values("name", "faculty__id", "id"))
        context["departments"] = json.dumps(faculty_list)
        programs = Program.objects.all().order_by("name")
        program_list = list(programs.values("name", "department__id", "id"))
        context["programs"] = json.dumps(program_list)
        return context

    def form_valid(self, form):
        form.instance.is_active = True
        return super(RegistrationView, self).form_valid(form)


@method_decorator(user_passes_test(lambda user: user.is_superuser), name="dispatch")
class StudentListView(generic.ListView):
    model = Student
    context_object_name = "students"
    template_name = "student/list.html"


@method_decorator(login_required(login_url="/login/"), name="dispatch")
class ProfileUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = StudentProfile
    form_class = StudentProfileForm
    success_message = "Profile has been updated successfully."
    template_name = "auth/profile_update.html"
    success_url = reverse_lazy('users:students')


@method_decorator(login_required(login_url="/login/"), name="dispatch")
class StudentProfileView(generic.TemplateView):
    template_name = "auth/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = StudentProfile.objects.get(user_id=kwargs['pk'])
        context['courses'] = CourseSchedule.objects.filter(students__in=[self.request.user.id])
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name="dispatch")
class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentSingUpForm
    success_url = reverse_lazy("users:students")
    template_name = "student/create.html"

    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        faculties = Faculty.objects.all().order_by("name")
        faculty_list = list(faculties.values("name", "id"))
        context["faculties"] = json.dumps(faculty_list)
        departments = Department.objects.all().order_by("name")
        faculty_list = list(departments.values("name", "faculty__id", "id"))
        context["departments"] = json.dumps(faculty_list)
        programs = Program.objects.all().order_by("name")
        program_list = list(programs.values("name", "department__id", "id"))
        context["programs"] = json.dumps(program_list)
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name="dispatch")
class StudentUpdateView(generic.UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("users:students")
    template_name = "student/update.html"


@method_decorator(user_passes_test(lambda user: user.is_superuser), name="dispatch")
class StudentDeleteView(generic.DeleteView):
    model = User
    success_url = reverse_lazy("users:students")

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)
