from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from portal.models import Ebook
from portal.forms.ebook_form import BookForm


class BooksListView(LoginRequiredMixin, generic.ListView):
    model = Ebook
    context_object_name = 'books'
    template_name = 'book/list.html'


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ebook
    template_name = 'book/detail.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class BookCreateView(SuccessMessageMixin, generic.CreateView):
    form_class = BookForm
    success_url = reverse_lazy('portal:books')
    success_message = 'Book Created successfully.'
    template_name = 'book/create.html'

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(BookCreateView, self).form_valid(form)


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class BookUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Ebook
    form_class = BookForm
    success_url = reverse_lazy('portal:books')
    success_message = 'Book successfully updated.'
    template_name = 'book/update.html'


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.teacher), name='dispatch')
class BookDeleteView(generic.DeleteView):
    model = Ebook
    success_url = reverse_lazy('portal:books')

    def get(self, *args, **kwargs):
        return self.delete(self.request, *args, **kwargs)
