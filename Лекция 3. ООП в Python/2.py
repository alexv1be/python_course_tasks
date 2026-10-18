class Ebook(Book):
    def __init__(self, title, author, year, book_format):
        super().__init__(title, author, year)
        self.format = book_format

    def info(self):
        return f"Электронная книга: '{self.title}', автор: {self.author}, год издания: {self.year}, формат: {self.format}"