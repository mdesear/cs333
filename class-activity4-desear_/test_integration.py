import unittest, book, wishlist, database

class TestDatabase(unittest.TestCase):
    def test_add_book_to_wishlist(self):
        test_book = book.Book("test1", "test2", "test3", "test4", "test5")
        test_list = wishlist.Wishlist("test")

        test_list.add_to_wishlist(test_book)

        self.assertEqual(test_book.title, test_list.list[0].title)
        self.assertEqual(test_book.author, test_list.list[0].author)
        self.assertEqual(test_book.price, test_list.list[0].price)
        self.assertEqual(test_book.isbn, test_list.list[0].isbn)
        self.assertEqual(test_book.genre, test_list.list[0].genre)

    def test_remove_book_from_wishlist(self):
        test_book = book.Book("test", "test", "test", "test", "test")
        test_list = wishlist.Wishlist("test")

        test_list.add_to_wishlist(test_book)
        test_list.remove_from_wishlist("0")

        self.assertEqual([], test_list.list)

    def test_add_book_to_database(self):
        test_book = book.Book("test1", "test2", "test3", "test4", "test5")
        test_database = database.Database()

        print("Please enter these values in order: test1, test2, test3, test4, test5")
        test_database.add_book()

        self.assertEqual(test_book.title, test_database.books[0].title)
        self.assertEqual(test_book.author, test_database.books[0].author)
        self.assertEqual(test_book.price, test_database.books[0].price)
        self.assertEqual(test_book.isbn, test_database.books[0].isbn)
        self.assertEqual(test_book.genre, test_database.books[0].genre)

    def test_remove_book_from_database(self):
        test_database = database.Database()

        print("You may enter arbitrary values for each field")
        test_database.add_book()
        test_database.remove_book("0")

        self.assertEqual([], test_database.books)

    def test_add_wishlist_to_database(self):
        test_wishlist = wishlist.Wishlist("test")
        test_database = database.Database()

        print("Please enter these values in order: test, 0, n")
        test_database.add_wishlist()

        self.assertEqual(test_wishlist.customer, test_database.wishlists[0].customer)
    
    def test_add_to_existing_wishlist(self):
        test_database = database.Database()
        test_book = book.Book("test1", "test2", "test3", "test4", "test5")

        print("Please enter these values in order: test1, test2, test3, test4, test5")
        test_database.add_book()

        print("Please enter these values in order: test, 0, n")
        test_database.add_wishlist()

        self.assertEqual(test_book.author, test_database.wishlists[0].list[0].author)

if __name__ == '__main__':
    unittest.main()