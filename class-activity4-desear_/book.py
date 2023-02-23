class Book:
    def __init__(self, title, author, price, isbn, genre):
        self.title = title
        self.author = author
        self.price = price
        self.isbn = isbn
        self.genre = genre

    def __str__(self):
        return f'{self.title} by {self.author}\nPrice: ${self.price}\nISBN: {self.isbn}\nGenre: {self.genre}'