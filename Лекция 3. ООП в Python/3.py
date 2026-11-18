"""Задача № 3. Сравнение книг, возраст и создание из строки."""

from datetime import datetime

class Book:
    """Книга со строковым представлением и вычисляемым возрастом."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        """Вернуть строку с названием, автором и годом издания."""
        return f"Книга: '{self.title}', автор: {self.author}, год издания: {self.year}"

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
