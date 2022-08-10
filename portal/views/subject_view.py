from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import generic
from portal.forms.subject_form import SubjectForm, EnrollSubjectForm
from portal.models import Subject, EnrollSubject


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class SubjectCreateListView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Subject
    paginate_by = 10
    form_class = SubjectForm
    success_url = '/subjects/'
    context_object_name = 'subjects'
    success_message = 'The subject has been created.'
    template_name = 'subject/subjects.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class SubjectUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Subject
    form_class = SubjectForm
    success_url = '/'
    success_message = 'The subject has been updated.'
    template_name = 'subject/update.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class SubjectDeleteView(generic.DeleteView):
    model = Subject
    success_url = '/subjects/'

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SubjectEnrollCreateAndListView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = EnrollSubject
    form_class = EnrollSubjectForm
    context_object_name = 'enrollSubjects'
    template_name = 'enroll/enroll.html'
    success_url = '/subjects/enroll/'
    success_message = 'subject has been enroll, pls wait for admin approve.'

    def get_queryset(self):
        queryset = super().get_queryset().filter(student=self.request.user)
        return queryset

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.student = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(SubjectEnrollCreateAndListView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SubjectEnrollUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = EnrollSubject
    form_class = EnrollSubjectForm
    template_name = 'enroll/update.html'
    success_url = '/subjects/enroll/'
    success_message = 'subject has been enroll, pls wait for admin approve.'

    def get_form_kwargs(self):
        kwargs = super(SubjectEnrollUpdateView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class EnrollApproveView(generic.UpdateView):
    model = EnrollSubject
    fields = ('is_approve',)
    template_name = 'enroll/aprove.html'
    success_url = '/'
    success_message = 'Subject has been enroll approve.'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class SubjectEnrollDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = EnrollSubject
    success_url = '/subjects/enroll/'

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)

