# query_samples.py

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1 - Query all books by a specific author
author = Author.objects.get(name="Jane Austen")
books = Book.objects.filter(author=author)
print("Books by Jane Austen:")
for book in books:
    print(book.title)

# 2 - List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("\nBooks in Central Library:")
for book in books_in_library:
    print(book.title)

# 3 - Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian for Central Library: {librarian.name}")
