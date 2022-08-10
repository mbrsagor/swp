from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from portal.models import Routine
from portal.forms.routine_form import RoutineForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RoutineCreateAndListView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Routine
    form_class = RoutineForm
    template_name = 'routine/routine.html'
    context_object_name = 'routine'
    success_url = '/routines/'
    success_message = 'Routine created'

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(RoutineCreateAndListView, self).form_valid(form)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RoutineUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Routine
    form_class = RoutineForm
    template_name = 'routine/update.html'
    success_url = '/routines/'
    success_message = 'Routine updated.'
    

@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RoutineDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Routine
    success_url = '/routines/'

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)