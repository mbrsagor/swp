from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from portal.models import Ebook
from portal.forms.ebook_form import BookForm


class BooksListView(LoginRequiredMixin, generic.ListView):
    model = Ebook
    context_object_name = 'books'
    template_name = 'teacher/books.html'


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ebook
    template_name = 'teacher/detail.html'


class BookCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Ebook
    form_class = BookForm
    template_name = 'teacher/books-create.html'
    success_url = '/books/'
    success_message = 'Book Created successfully.'

    def form_valid(self, form):
        form.instance.teacher = self.request.user
        return super(BookCreateView, self).form_valid(form)


class BookUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Ebook
    form_class = BookForm
    template_name = 'teacher/books-create.html'
    success_url = '/books/'
    success_message = 'Book updated successfully.'
