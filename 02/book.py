class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'"{self.title}" - {self.author} ({self.year})'


books = [
    Book("Python dla początkujących", 'Jan Kowalski', 2020),
    Book("Python dla początkujących v.2", 'Jan Kowalski', 2021),
    Book("Python dla zaawansowanych", 'Jan Kowalski', 2025)
]

for book in books:
    print(book)
