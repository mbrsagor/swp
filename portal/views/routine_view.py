from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from portal.models import Routine
from portal.forms.routine_form import RoutineForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class RoutineCreateAndListView(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Routine
    form_class = RoutineForm
    template_name = 'routine/list.html'
    context_object_name = 'routine'
    success_url = reverse_lazy('portal:routines')
    success_message = 'Routine successfully created'

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(RoutineCreateAndListView, self).form_valid(form)


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class RoutineUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Routine
    form_class = RoutineForm
    template_name = 'routine/update.html'
    success_url = reverse_lazy('portal:routines')
    success_message = 'Routine successfully updated.'
    

@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class RoutineDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Routine
    success_url = reverse_lazy('portal:routines')

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)