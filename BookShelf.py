#creating a stack to hold a finite number of books


def createShelf():
    shelf = []
    print(f"creates a Shelf to hold books in a LIFO {shelf}")
    return shelf

#method check whether the shelf is full

def shelfIsEmpty(shelf):
    if len(shelf) == 0:
        return f"{shelf} Stack is empty"
    else:
        return f" Stack is not empty it has {len(shelf)} books"


def addABookToShelf(shelf, book): #pushing an item to the stack
    shelf.append(book) #adding the book to the shelf
    return book

#remove books from the shelf
def removeBook(shelf):
    #check if the stack is empty 
    if len(shelf) == 0:
        return f"This shelf is empty and one cannot remove a book"
    else:
        return shelf.pop() #remove the book from the shelf
    # else:
    #     return f" the {book} does not exist in the shelf"


def displayShelf(shelf):
    print('Showing the shelf', shelf)
    return shelf

my_shelf = createShelf()
added_book = addABookToShelf(my_shelf,"Lester Principles")
added_book = addABookToShelf(my_shelf,"Calculus Principles")
added_book = addABookToShelf(my_shelf,"Computer Engineering")
added_book = addABookToShelf(my_shelf,"Chemistry")
print(added_book)
displayShelf(my_shelf)
check = shelfIsEmpty(my_shelf)
print(check)
removed = removeBook(my_shelf)
removed = removeBook(my_shelf)
print(removed)
displayShelf(my_shelf)