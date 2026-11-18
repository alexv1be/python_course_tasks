"""Чтение списка пород и фотографий через Dog API."""

from django.core.cache import cache

from api_http import ApiError, get_json

BASE_URL = "https://dog.ceo/api"


def _get_message(path):
    """Извлечь поле message из успешного ответа Dog API."""
    data = get_json(f"{BASE_URL}/{path}")
    if data.get("status") != "success":
        raise ApiError("Dog API не смог обработать запрос.")
    return data["message"]


def get_breeds():
    """Вернуть отсортированный список пород и подпород в формате breed/subbreed."""
    breeds = cache.get("dog_api_breeds")
    if breeds is None:
        groups = _get_message("breeds/list/all")
        breeds = list(groups)
        breeds.extend(
            f"{breed}/{subbreed}"
            for breed, subbreeds in groups.items()
            for subbreed in subbreeds
        )
        breeds.sort()
        cache.set("dog_api_breeds", breeds, timeout=3600)
    return breeds


def get_dog_image(breed):
    """Получить ссылку на случайную фотографию известной породы или подпороды."""
    return _get_message(f"breed/{breed}/images/random")
