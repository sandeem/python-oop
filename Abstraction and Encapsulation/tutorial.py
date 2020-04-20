# Class => Library
# Layers of abstraction => display available books, to lend a book
# and to add a book

# Class => Customer
# Layersof abstraction => request for a book, return a book


# Performed encapsulation within your classes and have hidden
# all implementation details within your main program and have 
# provided layers of abstraction by calling methods from your
# program which gave you access to the data within your class
class Library:
    
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    
    def displayAvailableBooks(self):
      #  print()
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)
    
    def lendBook(self, requestededBook):
        if requestedBook in self.availableBooks:
            print("You have now borrowed the book")
            self.availableBooks.remove(requestededBook)
        else:
            print("Sorry, the book is not available in our list")
    
    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("YOu have returned the book. Thank you!")
    
class Customer:
    def requestBook(self):
        print("Enter the name of the book you would like to borrow: ")
        self.book = input()
        return self.book
    
    def returnBook(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book
# when you are passing a list of arguments (name of books), you should
# have __init__ method to initialize these      
library = Library(['Think and Grow Rich', 'Who Will Cry When You Die',
                    'For One More Day']) 
customer = Customer()
while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()

    
