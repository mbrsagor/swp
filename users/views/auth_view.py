from django.shortcuts import resolve_url, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.views import generic, View
from users.forms.auth_form import LoginForm


# class DashboardView(LoginRequiredMixin, generic.TemplateView):
#     template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if self.request.user.roll == 'STUDENT':
    #         context['routine'] = Routine.objects.all()

        # if self.request.user.roll == 'TEACHER':
        #     context['routine'] = Routine.objects.filter(book=self.request.user)
        #
        # if self.request.user.is_superuser:
        #     context['subjects'] = Subject.objects.all()
        #     context['enroll_subjects'] = EnrollSubject.objects.all()

        # return context


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
