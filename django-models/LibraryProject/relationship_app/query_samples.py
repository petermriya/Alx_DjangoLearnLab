# querysamples.py

# Import the models so we can use them in our queries
from relationship_app.models import Author, Book, Library, Librarian

# 1. Find all books written by a specific author
def get_books_by_author(author_name):
    # Try to find the author by name
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        print("Author not found.")
        return []

    # Get all books written by that author
    books = Book.objects.filter(author=author)
    return books

# 2. List all books available in a specific library
def get_books_in_library(library_name):
    # Try to find the library by name
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print("Library not found.")
        return []

    # Get all books in the library (ManyToMany relationship)
    books = library.books.all()
    return books

# 3. Find the librarian who works in a specific library
def get_librarian_for_library(library_name):
    # Try to find the library
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print("Library not found.")
        return None

    # Try to find the librarian linked to that library
    try:
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Librarian.DoesNotExist:
        print("Librarian not found.")
        return None
