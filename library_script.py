from library import Book

books = [
    Book("My Dark Vanessa", "Keith Rassel", 2020, 1599, 4.0),
    Book("Strange Sally Diamond", "Liz Nugent", 2023, 2300, 4.8),
    Book("Deep Water", "Patricia Highsmith", 1957, 1275, 3.5)]

for book in books:
    print(book.get_info())

most_expensive_book = Book.find_most_expensive(books)
print(f"\nMost Expensive Book: {most_expensive_book.get_info()}")
highest_rated_book = max(books, key=lambda book: book.raiting)
print(f"\nHighest Rated Book: {highest_rated_book.get_info()}")

author_to_censor = "Keith Rassel"
books[0].censor(author_to_censor, True)
print(f"\nAfter censoring {author_to_censor}:")
filtered_books = [book for book in books if not book.stoplist]

print(f"\nBooks after censoring {author_to_censor}:")
for book in filtered_books:
    print(book.get_info())