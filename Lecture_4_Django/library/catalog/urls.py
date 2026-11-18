"""Маршруты учебного каталога и галереи собак."""

from django.urls import path

from . import views

app_name = "catalog"
urlpatterns = [
    path("", views.book_list, name="book_list"),
    path("books/<int:book_id>/", views.book_detail, name="book_detail"),
    path("dogs/", views.dog_gallery, name="dog_gallery"),
]
