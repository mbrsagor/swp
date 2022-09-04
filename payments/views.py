from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views import generic
from django.urls import reverse_lazy
from payments.models import Payment
from payments.forms import PaymentForm


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class PaymentListView(generic.ListView):
    model = Payment
    context_object_name = 'payments'
    template_name = 'payment/list.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class PaymentCreateView(generic.CreateView):
    form_class = PaymentForm
    model = Payment
    success_url = reverse_lazy('payments:payments')
    template_name = 'payment/create.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class PaymentUpdateView(generic.UpdateView):
    model = Payment
    form_class = PaymentForm
    success_url = reverse_lazy('payments:payments')
    template_name = 'payment/update.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser), name='dispatch')
class PaymentDeleteView(generic.DeleteView):
    model = Payment
    success_url = reverse_lazy('payments:payments')

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)
    
