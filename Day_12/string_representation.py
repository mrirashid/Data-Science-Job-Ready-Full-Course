# str VS repr
class Book:
    def __str__(self):
        return "Readable title for users"
    
    def __repr__(self):
        return "Book(id=101, title='Code')"

book = Book()   # object created

print(book)        # calls __str__
list_of_books = [book]
print(list_of_books) # calls __repr__
