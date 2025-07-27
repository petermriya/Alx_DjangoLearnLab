# relationship_app/views.py

from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Book, Library

# Function-Based View: List all books with their authors
def list_books(request):
    books = Book.objects.select_related('author').all()
    lines = [f"{book.title} by {book.author.name}" for book in books]
    return HttpResponse("\n".join(lines), content_type="text/plain")

# Class-Based View: Detail view of a library with its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.select_related('author').all()
        return context
