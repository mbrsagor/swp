from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import generic, View
from users.forms import LoginForm, StudentSingUpForm, StudentProfileForm, TeacherSingUpForm, TeacherProfileForm, \
    UserForm
from portal.models import Subject, EnrollSubject
from users.models import User, Teacher, Student, StudentProfile, TeacherProfile


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'
    	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        context['enroll_subjects'] = EnrollSubject.objects.filter(student=self.request.user)
        return context


# Student view
@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class StudentListView(generic.ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student/list.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class StudentCreateView(generic.CreateView):
    model = Student
    form_class = StudentSingUpForm
    success_url = '/students/'
    template_name = 'student/create.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class StudentUpdateView(generic.UpdateView):
    model = User
    form_class = UserForm
    template_name = 'student/update.html'
    success_url = '/students/'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class StudentDeleteView(generic.DeleteView):
    model = User
    success_url = '/students/'

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)
# end start view


# teahers views
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
    success_url = '/teachers/'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class TeacherUpdateView(generic.UpdateView):
    model = User
    form_class = UserForm
    template_name = 'teacher/update.html'
    success_url = '/teachers/'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class TeacherDeleteView(generic.DeleteView):
    model = User
    success_url = '/teachers/'

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)


class SingInView(LoginView):
    authentication_form = LoginForm
    form_class = LoginForm
    redirect_authenticated_user = False
    template_name = 'auth/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url('/dashboard/')

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        print('form working.')
        login(self.request, form.get_user())

        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(SingInView, self).form_valid(form)

    def form_invalid(self, form):
        print('invalid form')
        return super(SingInView, self).form_invalid(form)


class SignOutView(View):

    def get(self, request):
        logout(request)
        return redirect('/login/')


class RegistrationView(SuccessMessageMixin, generic.CreateView):
    form_class = StudentSingUpForm
    success_url = '/login/'
    success_message = 'Successfully registration done.'
    template_name = 'auth/register.html'

    def form_valid(self, form):
        form.instance.is_active = True
        return super(RegistrationView, self).form_valid(form)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfileUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = StudentProfile
    form_class = StudentProfileForm
    success_message = 'Profile has been updated successfully.'
    template_name = 'auth/profile_update.html'

    def get_success_url(self):
        return reverse('profile', kwargs={
            'pk': self.object.pk,
        })


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class StudentProfileView(generic.ListView):
    model = StudentProfile
    context_object_name = 'profile'
    template_name = 'auth/profile.html'

    def get_queryset(self):
        try:
            return StudentProfile.objects.get(user=self.request.user)
        except Exception as ex:
            print(ex)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TeacherProfileView(generic.ListView):
    model = TeacherProfile
    context_object_name = 'profile'
    template_name = 'teacher/profile.html'

    def get_queryset(self):
        try:
            return TeacherProfile.objects.get(user=self.request.user)
        except Exception as ex:
            print(ex)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TeacherProfileUpdateView(generic.UpdateView):
    model = TeacherProfile
    form_class = TeacherProfileForm
    template_name = 'teacher/profile-update.html'

    def get_success_url(self):
        return reverse('teachers-profile-view', kwargs={
            'pk': self.object.pk,
        })

    def get_form_kwargs(self):
        kwargs = super(TeacherProfileUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
