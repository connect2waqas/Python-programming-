class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def get_info(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # Initialize an empty list of books
    
    def add_book(self, book):
        # Add a book to the library's collection
        self.books.append(book)
    
    def show_books(self):
        print(f"Books in {self.name} Library:")
        for book in self.books:
            print(book.get_info())

# Create book instances
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Create a library instance and add books to it
library = Library("City Library")
library.add_book(book1)
library.add_book(book2)

# Show books in the library
library.show_books()

class Book:
    def __init__(self, title , author):
        self.name = title
        self.author = author
    
    def get_info(self):
        return f"'{self.title}' by {self.author}"

        