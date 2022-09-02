from django.shortcuts import resolve_url, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.views import View
from users.forms.auth_form import LoginForm


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
