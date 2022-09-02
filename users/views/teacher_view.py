from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from users.models import User, Teacher, TeacherProfile
from users.forms.teacher_form import TeacherSingUpForm, TeacherProfileForm, TeacherForm


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class TeacherListView(generic.ListView):
    model = Teacher
    context_object_name = 'teachers'
    template_name = 'teacher/list.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class TeacherCreateView(generic.CreateView):
    model = Teacher
    form_class = TeacherSingUpForm
    template_name = 'teacher/create.html'
    success_url = reverse_lazy('users:teachers')


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class TeacherUpdateView(generic.UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/update.html'
    success_url = reverse_lazy('users:teachers')


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class TeacherDeleteView(generic.DeleteView):
    model = User
    success_url = reverse_lazy('users:teachers')

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TeacherProfileView(generic.TemplateView):
    template_name = 'teacher/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = TeacherProfile.objects.get(user_id=kwargs['pk'])
        return context


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class TeacherProfileUpdateView(generic.UpdateView):
    model = TeacherProfile
    form_class = TeacherProfileForm
    template_name = 'teacher/profile-update.html'
    success_url = reverse_lazy('users:teachers')

    def get_form_kwargs(self):
        kwargs = super(TeacherProfileUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
