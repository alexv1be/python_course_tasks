"""Задача № 1. Класс книги и её текстовое описание."""


class Book:
    """Хранит название, автора и год издания книги."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        """Вернуть строку с названием, автором и годом издания."""
        return f"Книга: '{self.title}', автор: {self.author}, год издания: {self.year}"
