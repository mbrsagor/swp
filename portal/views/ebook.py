from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from ..models.ebook import Ebook
from ..forms.ebook import BookForm


class BooksListView(LoginRequiredMixin, generic.ListView):
    model = Ebook
    context_object_name = 'books'
    template_name = 'teacher/books.html'


class BookCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = Ebook
    form_class = BookForm
    template_name = 'teacher/books-create.html'
    success_url = '/books/'
    success_message = 'Book Created successfully.'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.teacher = self.request.user
        instance.save()
        return super(BookCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs = super(BookCreateView, self).get_context_data(**kwargs)
        kwargs['title'] = 'Book create'
        return kwargs


class BookUpdateView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Ebook
    form_class = BookForm
    template_name = 'teacher/books-create.html'
    success_url = '/books/'
    success_message = 'Book updated successfully.'

    # def form_valid(self, form):
    #     instance = form.save(commit=False)
    #     instance.teacher = self.request.user
    #     instance.save()
    #     return super(BookCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs = super(BookUpdateView, self).get_context_data(**kwargs)
        kwargs['title'] = 'Book Update'
        return kwargs
