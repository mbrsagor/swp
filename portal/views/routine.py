from .views import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RoutineView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Routine
    form_class = RoutineForm
    template_name = 'routine/routine.html'
    context_object_name = 'routine'
    success_url = '/routine/'
    success_message = 'Routine created'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RoutineDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Routine
    template_name = 'common/delete_confirm.html'
    success_url = '/routine/'
    success_message = 'Routine deleted'
