from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Книга: '{self.title}', автор: {self.author}, год издания: {self.year}"

    # Магический метод __str__
    def __str__(self):
        return self.info()

    # Магический метод __eq__ для сравнения
    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title and
                    self.author == other.author and
                    self.year == other.year)
        return False

    # Свойство для возраста книги
    @property
    def age(self):
        return datetime.now().year - self.year

    # Классовый метод для создания книги из строки
    @classmethod
    def from_string(cls, data):
        title, author, year = data.split(';')
        return cls(title, author, int(year))