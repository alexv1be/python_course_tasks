"""Регистрация каталога книг в админке Django."""

from django.contrib import admin

from .models import Book

admin.site.register(Book)
