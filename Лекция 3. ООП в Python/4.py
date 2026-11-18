"""Задача № 4. Абстрактный интерфейс печати для книг."""

from abc import ABC, abstractmethod
from datetime import datetime

class Printable(ABC):
    """Интерфейс для объектов, которые умеют печатать своё описание."""

    @abstractmethod
    def print_info(self):
        """Напечатать описание объекта."""

class Book(Printable):
    """Книга, реализующая интерфейс Printable."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        """Вернуть строку с названием, автором и годом издания."""
        return f"Книга: '{self.title}', автор: {self.author}, год издания: {self.year}"

    def print_info(self):
        """Напечатать описание, полученное из info()."""
        print(self.info())

    def __str__(self):
        """Вернуть описание для str() и print()."""
        return self.info()

    def __eq__(self, other):
        """Сравнить книги по названию, автору и году издания."""
        if isinstance(other, Book):
            return (self.title == other.title and
                    self.author == other.author and
                    self.year == other.year)
        return False

    @property
    def age(self):
        """Вернуть разницу между текущим годом и годом издания."""
        return datetime.now().year - self.year

    @age.setter
    def age(self, years):
        """Пересчитать год издания при присваивании возраста в годах."""
        self.year = datetime.now().year - years

    @classmethod
    def from_string(cls, data):
        """Создать книгу из строки формата «название;автор;год»."""
        title, author, year = data.split(';')
        return cls(title, author, int(year))

class Ebook(Book):
    """Электронная книга с форматом файла и поддержкой печати."""

    def __init__(self, title, author, year, book_format):
        super().__init__(title, author, year)
        self.format = book_format

    def info(self):
        """Вернуть описание электронной книги с указанием её формата."""
        return f"Электронная книга: '{self.title}', автор: {self.author}, год издания: {self.year}, формат: {self.format}"

    @classmethod
    def from_string(cls, data):
        """Создать электронную книгу из строки «название;автор;год;формат»."""
        title, author, year, book_format = data.split(';')
        return cls(title, author, int(year), book_format)
