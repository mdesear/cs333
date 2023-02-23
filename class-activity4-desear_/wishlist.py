class Wishlist:
    def __init__(self, customer):
        self.list = list()
        self.customer = customer

    def print_wishlist(self):
        print(f'{self.customer}\'s wishlist: ')

        for i in range(len(self.list)):
            print(str(i) + '. ' + self.list[i].__str__())

    def add_to_wishlist(self, book):
        self.list.append(book)

    def remove_from_wishlist(self, index):
        del self.list[int(index)]
