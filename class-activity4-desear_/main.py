import database, pickle

def main():  
    try: 
        with open('database.pkl', 'rb') as f:
            db = pickle.load(f)
    except: 
        db = database.Database()
    while True:  
        prompt = True
        while prompt:
            print('\nWelcome to the bookstore database!\n1) View and manage inventory\n2) View and manage wishlists\n3) Exit database')
            view_choice = input('Please enter the number of the option you\'d like to select: ')
            match view_choice:
                case "1":
                    db.print_inventory()
                    print ('\n1) Add book\n2) Remove book\n3) Back')
                    manage_choice = input('Please enter the number of the option you\'d like to select: ')        
                    match manage_choice:
                        case "1":
                            db.add_book()
                        case "2":
                            if db.books != []:
                                index = input('\nEnter the index number of the book you\'d like to remove: ')
                                try:
                                    db.remove_book(index)
                                    print('Book successfully removed.')
                                except:
                                    print('Invalid choice. Please try again.')
                                    continue
                            else:
                                print("There are no books to remove!\n")
                        case "3": 
                            break  
                        case _: 
                            print('Invalid choice. Please try again.')
                            continue      
                case "2":
                    db.print_wishlists()
                    print('\n1) Add a wishlist\n2) Delete a wishlist\n3) Edit an existing wishlist\n4) Back')
                    wish_choice = input('Please enter the number of the option you\'d like to select: ')
                    match wish_choice:
                        case "1":
                            db.add_wishlist()
                        case "2":
                            if db.wishlists != []:
                                index = input('Enter the index number of the wishlist you\'d like to remove: ')
                                try:
                                    db.remove_wishlist(index)
                                    print('Wishlist successfully removed.')
                                except:
                                    print('Invalid choice. Please try again.')
                                    continue
                            else:
                                print("There are no wishlists to remove!\n")
                        case "3":
                            if db.wishlists != []:
                                edit_choice = input("Enter the index of the wishlist you'd like to edit: ")
                                add_remove_choice = input("Would you like to 1) add or 2) remove a book?: ")
                                if add_remove_choice == "1":
                                    db.print_inventory
                                    book_index = input("Enter the index of the book you'd like to add to this list: ")
                                    try: 
                                        db.wishlists[int(edit_choice)].add_to_wishlist(db.books[int(book_index)])
                                        print("Book successfully added.")
                                    except: 
                                        print("Invalid entry. Please try again.")
                                        continue
                                elif add_remove_choice == "2":
                                        db.wishlists[int(edit_choice)].print_wishlist()
                                        book_index = input("Enter the index of the book you'd like to remove from this list: ")
                                        try:
                                            db.wishlists[int(edit_choice)].remove_from_wishlist(int(book_index))
                                            print("Book successfully removed.")
                                        except:
                                            print("invalid entry. Please try again.")
                                            continue
                                else:
                                    print("Invalid choice. Please try again.")
                                    continue
                            else:
                                print("There are no wishlists to edit!\n")
                case "3":
                    print("Saving database to database.pkl...")
                    with open('database.pkl', 'wb') as f:
                        pickle.dump(db, f)
                    quit()
                case _:
                    print('Invalid choice. Please try again.')
                    continue
                
if __name__ == '__main__':
    main()