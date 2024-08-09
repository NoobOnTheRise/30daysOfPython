# Write a Library class with no_of_books and books as two instance variables. 
# Write a program to create a library from this Library class and 
# show how you can print all books, 
# add a book and 
# get the number of books using different methods. 
# Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def get_no_of_books(self):
        return self.no_of_books

    def print_books(self):
        for book in self.books:
            print(book)

a = Library()
a.add_book("Harry Potter 1")
a.add_book("Harry Potter 2")
a.add_book("Harry Potter 3")
a.print_books()
print(a.get_no_of_books())
b = Library()
b.add_book("Lord of the Rings 1")
b.add_book("Lord of the Rings 2")
b.add_book("Lord of the Rings 3")
b.print_books()
print(b.get_no_of_books())