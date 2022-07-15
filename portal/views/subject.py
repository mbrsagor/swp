from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic

from portal.forms.subject import SubjectForm, EnrollSubjectForm
from portal.models.subject import Subject, EnrollSubject


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SubjectCreateListView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Subject
    paginate_by = 10
    form_class = SubjectForm
    success_url = '/subjects/'
    context_object_name = 'subjects'
    success_message = 'The subject has been created.'
    template_name = 'subject/subjects.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
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

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.student = self.request.user
        instance.save()
        form.save_m2m()
        return super().form_valid(form)


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class EnrollApproveConfirmed(generic.View):
    """
    just access admin
    """
    def get(self, *args, **kwargs):
        try:
            enroll_subject = EnrollSubject.objects.get(pk=kwargs['pk'])
            if enroll_subject.is_approve:
                enroll_subject.is_approve = False
                enroll_subject.save()
                return redirect('subject_enroll')
            enroll_subject.is_approve = True
            enroll_subject.save()
            print(enroll_subject.is_approve)
            return redirect('subject_enroll')
        except:
            return redirect('subject_enroll')


class SubjectEnrollDeleteView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = EnrollSubject
    success_url = '/subjects/enroll/'

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)

