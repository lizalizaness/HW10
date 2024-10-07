class Book:
    def __init__(self, title, author, year, price, raiting, stoplist=False):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist
        self.raiting = raiting
    def get_info(self):
        return f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Price: {self.price}, Stoplist: {self.stoplist}, Raiting: {self.raiting}"
    @classmethod
    def find_most_expensive(cls, books):
        return max(books, key=lambda book: book.price)
    def set_stoplist(self, value):
        if isinstance(value, bool):
            self.stoplist = value
        else:
            raise ValueError("stoplist must be a boolean value (True or False)")
    def censor(self, author_name, value):
        if self.author == author_name:
            if isinstance(value, bool):
                self.stoplist = value
            else:
                raise ValueError("Value must be a boolean (True or False)")