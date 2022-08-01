from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import resolve_url, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test, login_required
from django.views import generic, View

from users.forms import SingUpForm, ProfileUpdateForm
from users.models import Profile
from portal.models.subject import Subject, EnrollSubject


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'

    	
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjects'] = Subject.objects.all()
        context['enroll_subjects'] = EnrollSubject.objects.all()
        return context

    


class SingInView(generic.TemplateView):
    template_name = 'auth/login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                next = request.META['HTTP_REFERER']
                return HttpResponseRedirect(next)
        else:
            next = request.META['HTTP_REFERER']
            return HttpResponseRedirect(next)


class SignOutView(View):

    def get(self, request):
        logout(request)
        return redirect('/login/')


class RegistrationView(SuccessMessageMixin, generic.CreateView):
    form_class = SingUpForm
    success_url = '/login/'
    success_message = 'Successfully registration done.'
    template_name = 'auth/register.html'

    def form_valid(self, form):
        form.instance.is_active = True
        return super(RegistrationView, self).form_valid(form)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfileUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    success_message = 'Profile has been updated successfully.'
    template_name = 'auth/profile_update.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user.id)

    def get_success_url(self):
        return reverse('profile_update', kwargs={
            'pk': self.object.pk,
        })


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfileView(generic.ListView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'auth/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        try:
            return Profile.objects.get(user=self.request.user)
        except Exception as ex:
            print(ex)
