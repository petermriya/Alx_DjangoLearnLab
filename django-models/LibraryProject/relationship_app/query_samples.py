from relationship_app.models import Author, Book, Library, Librarian

books_by_author = Book.objects.filter(author__name="Author Name")
books_in_library = Library.objects.get(name="Library Name").books.all()
librarian = Librarian.objects.get(library__name="Library Name")

