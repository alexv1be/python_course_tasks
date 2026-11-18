"""HTTP GET и обработка ошибок для учебных практик."""

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


class ApiError(Exception):
    """Не удалось получить данные от внешнего сервиса."""


class ApiNotFound(ApiError):
    """Внешний сервис не нашёл запрошенный ресурс."""


def get_json(url):
    """Отправить GET-запрос с ограничением времени ожидания и прочитать JSON."""
    request = Request(
        url,
        headers={"Accept": "application/json", "User-Agent": "django-course-library/1.0"},
    )
    try:
        with urlopen(request, timeout=5) as response:
            return json.load(response)
    except HTTPError as error:
        if error.code == 404:
            raise ApiNotFound("Ресурс не найден.") from error
        raise ApiError(f"Сервис вернул ошибку HTTP {error.code}.") from error
    except (URLError, OSError) as error:
        raise ApiError("Сервис недоступен. Проверьте подключение к интернету.") from error
    except ValueError as error:
        raise ApiError("Сервис вернул некорректный JSON.") from error
