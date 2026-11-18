"""Модель книги для учебного каталога."""

from django.db import models


class Book(models.Model):
    """Книга с названием, автором и необязательным описанием."""

    title = models.CharField("Название", max_length=200)
    author = models.CharField("Автор", max_length=200)
    description = models.TextField("Описание", blank=True)

    def __str__(self):
        """Вернуть название для отображения книги в админке."""
        return self.title
