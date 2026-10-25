class Book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self. is_borrowed = True
        print(f"Confirmed: '{self.title}' has been returned.")

    def return_book(self):
        self.is_borrowed = False
        print(f"Confirmed: '{self.title}' has been returned.")

b1 = Book("1984", "George Orwell")
b2 = Book("The Hobbit" "J.R.R.Tolkien")
b3 = Book("The Stranger","Albert Camus")

b1.borrow()
b2.return_book()
b3.borrow()
