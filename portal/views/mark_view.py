from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views import generic
from django.urls import reverse_lazy
from portal.models import Mark
from portal.forms.mark_form import MarkForm
from users.models import StudentProfile
from django.db.models import Q


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class MarkListView(generic.CreateView,  generic.ListView):
    model = Mark
    form_class = MarkForm
    success_url = reverse_lazy('portal:marks')
    template_name = 'mark/list.html'

    def get_queryset(self):
        qs = super(MarkListView, self).get_queryset()
        if self.request.user.teacher:
            return qs.filter(teacher=self.request.user)
        else:
            return qs.all()
    
    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(MarkListView, self).form_valid(form)


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class MarkUpdateView(generic.UpdateView):
    model = Mark
    form_class = MarkForm
    success_url = reverse_lazy('portal:marks')
    template_name = 'mark/update.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class MarkDeleteView(generic.DeleteView):
    model = Mark
    success_url = reverse_lazy('portal:marks')

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class MarkSearchView(generic.ListView):
    model = Mark
    template_name = 'mark/search.html'

    def get_queryset(self):
        if not (query := self.request.GET.get("q")):
            return self.model.objects.none()
        if self.request.user.teacher:
            profile = StudentProfile.objects.get(unique_id__icontains=query)
            return self.model.objects.filter(
                (Q(student__username__icontains=profile.user.username) & Q(teacher=self.request.user)))

        else:
            profile = StudentProfile.objects.get(unique_id__icontains=query)
            return self.model.objects.filter(Q(student__username__icontains=profile.user.username))
