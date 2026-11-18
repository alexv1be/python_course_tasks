"""Представления каталога и страницы с фотографиями собак."""

from django.shortcuts import get_object_or_404, render

from api_http import ApiError

from .dog_api import get_breeds, get_dog_image
from .models import Book


def book_list(request):
    """Показать каталог и ссылки на страницы книг."""
    books = Book.objects.order_by("title", "pk")
    return render(request, "book_list.html", {"books": books})


def book_detail(request, book_id):
    """Показать карточку книги или вернуть 404 по неизвестному идентификатору."""
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "book_detail.html", {"book": book})


def dog_gallery(request):
    """Показать список пород и получить по одному фото для каждой выбранной породы."""
    entered = request.GET.get("breeds", "")
    selected = dict.fromkeys(breed.strip().lower() for breed in entered.split(","))
    breeds = []
    photos = []
    errors = []
    try:
        breeds = get_breeds()
    except ApiError as error:
        errors.append(f"Список пород недоступен. {error}")
    else:
        for breed in selected:
            if not breed:
                continue
            if breed not in breeds:
                errors.append(f"Порода «{breed}» отсутствует в списке.")
                continue
            try:
                photos.append((breed, get_dog_image(breed)))
            except ApiError as error:
                errors.append(f"Не удалось получить фото породы «{breed}». {error}")
        if "breeds" in request.GET and not any(selected):
            errors.append("Введите хотя бы одну породу.")

    return render(
        request,
        "dog_gallery.html",
        {"breeds": breeds, "entered": entered, "photos": photos, "errors": errors},
    )
