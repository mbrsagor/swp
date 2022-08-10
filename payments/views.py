from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views import generic
from payments.models import Payment
from payments.forms import PaymentForm


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class PaymentListView(generic.ListView):
    model = Payment
    context_object_name = 'payments'
    template_name = 'payments/list.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class PaymentCreateView(generic.CreateView):
    form_class = PaymentForm
    template_name = 'payments/create.html'
    success_url = '/payments/'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class PaymentUpdateView(generic.UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payments/update.html'
    success_url = '/payments/'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class PaymentDeleteView(generic.DeleteView):
    model = Payment
    success_url = '/payments/'

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)
    
