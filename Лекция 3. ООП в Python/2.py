"""Задача № 2. Электронная книга как разновидность книги."""

from importlib import import_module

# Имя файла совпадает с номером задачи, поэтому импортируем его по строке.
Book = import_module("1").Book


class Ebook(Book):
    """Книга с дополнительным атрибутом формата, например EPUB."""

    def __init__(self, title, author, year, book_format):
        super().__init__(title, author, year)
        self.format = book_format

    def info(self):
        """Вернуть описание электронной книги с указанием её формата."""
        return f"Электронная книга: '{self.title}', автор: {self.author}, год издания: {self.year}, формат: {self.format}"
