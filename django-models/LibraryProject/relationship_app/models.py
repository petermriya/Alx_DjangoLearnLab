from django.db import models

# Create your models here.

# Each Author has just a name
class Author(models.Model):
    name = models.CharField(max_length=100)  # Name of the author

    def __str__(self):
        return self.name  # Makes it easy to see names in admin/shell

# Each Book has a title and is linked to ONE Author
class Book(models.Model):
    title = models.CharField(max_length=100)  # Title of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Connect to an author

    def __str__(self):
        return self.title

# Each Library has a name and MANY books
class Library(models.Model):
    name = models.CharField(max_length=100)  # Name of the library
    books = models.ManyToManyField(Book)  # A library can have many books, and a book can be in many libraries

    def __str__(self):
        return self.name

# Each Librarian has a name and is linked to ONE Library only
class Librarian(models.Model):
    name = models.CharField(max_length=100)  # Name of the librarian
    library = models.OneToOneField(Library, on_delete=models.CASCADE)  # One-to-one link with Library

    def __str__(self):
        return self.name
