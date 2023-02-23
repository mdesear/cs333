import book, wishlist

class Database:
    def __init__(self):
        self.books = list()
        self.wishlists = list()

    def remove_book(self, index):
        del self.books[int(index)]

    def print_inventory(self):
        if self.books != []:
            for i in range(len(self.books)):
                print("\n" + str(i) + ") " + self.books[i].__str__())
        else:
            print("\nThere are currently no books in the inventory.")

    def print_wishlists(self):
        if self.wishlists != []:
            for i in range(len(self.wishlists)):
                print("\n" + str(i) + ") ")
                self.wishlists[i].print_wishlist()
        else:
            print("\nThere are currently no wishlists.")

    def add_book(self):
        print("\nPlease enter the information for each field.")
        title = input("Title: ")
        author = input("Author (last, first): ")
        price = input("Price (excluding dollar sign): ")
        isbn = input("ISBN (excluding dashes): ")
        genre = input("Genre: ")
        new_book = book.Book(title, author, price, isbn, genre)
        self.books.append(new_book)
        print("Book successfully added.")
    
    def add_wishlist(self):
        enter_books = True
        print("\nPlease enter the information for each field.")
        name = input("Customer name (last, first): ")
        new_list = wishlist.Wishlist(name)
        while enter_books:
                self.print_inventory()
                index = input("Book inventory index: ")
                if self.books != []:
                    try:
                        book_to_add = self.books[int(index)]
                    except:
                        print("A book with that index does not exist. Please try again.")
                        continue
                    new_list.add_to_wishlist(book_to_add)
                else:
                    print("There are no books to add to this wishlist!")
                yes_no = input("Would you like to input another book? (Y/N): ")
                if str.lower(yes_no) == "y":
                    continue
                elif str.lower(yes_no) == "n":
                    self.wishlists.append(new_list)
                    break
                else:
                    print("Please enter a valid option.")
                    continue

    def remove_wishlist(self, index):
        del self.wishlists[int(index)]


            
