class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Книга: '{self.title}', автор: {self.author}, год издания: {self.year}"