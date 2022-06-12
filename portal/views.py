from django.urls import reverse
from django.views import View, generic
from django.shortcuts import redirect
from django.shortcuts import resolve_url
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import user_passes_test, login_required

from .forms import LoginForm, SingUpForm, ProfileUpdateForm
from .models import Profile


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class DashboardView(generic.TemplateView):
    template_name = 'index.html'


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
        login(self.request, form.get_user())

        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(SingInView, self).form_valid(form)


class SignOutView(View):

    def get(self, request):
        logout(request)
        return redirect('/login/')


class RegistrationView(SuccessMessageMixin, generic.CreateView):
    form_class = SingUpForm
    success_url = '/login/'
    success_message = 'Successfully registration done.'
    template_name = 'auth/register.html'


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

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
