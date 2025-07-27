from .models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """
    Query all books by a specific author.
    Returns a queryset of books written by the author with the given name.
    """
    return Book.objects.filter(author__name=author_name)

def get_books_in_library(library_name):
    """
    List all books in a specific library.
    Returns a queryset of books associated with the library with the given name.
    """
    return Book.objects.filter(libraries__name=library_name)

def get_librarian_for_library(library_name):
    """
    Retrieve the librarian for a specific library.
    Returns the Librarian object associated with the library with the given name.
    """
    return Librarian.objects.get(library__name=library_name)
