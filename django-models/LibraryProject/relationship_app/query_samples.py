from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author (e.g., "George Orwell")
author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print("Books by George Orwell:", books_by_author)

# 2. List all books in a specific library (e.g., "Central Library")
library = Library.objects.get(name="Central Library")
books_in_library = library.book.all()
print("Books in Central Library:", books_in_library)

# 3. Retrieve the librarian for a specific library (e.g., "Central Library")
librarian = Librarian.objects.get(library__name="Central Library")
print("Librarian of Central Library:", librarian)