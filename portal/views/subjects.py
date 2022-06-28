from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .views import *


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SubjectCreateListView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Subject
    paginate_by = 10
    form_class = SubjectForm
    success_url = '/subject/'
    context_object_name = 'subject'
    success_message = 'The subject has been created.'
    template_name = 'subject/subject_listview.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class SubjectDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Subject
    success_url = '/subject/'
    success_message = 'Subject has been deleted.'
    template_name = 'common/delete_confirm.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class EnrollSubjectView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = EnrollSubject
    form_class = EnrollSubjectForm
    context_object_name = 'enrollSubject'
    template_name = 'enroll/enroll.html'
    success_url = '/subject/subject-enroll'
    success_message = 'subject has been enroll, pls wait for admin approve.'
