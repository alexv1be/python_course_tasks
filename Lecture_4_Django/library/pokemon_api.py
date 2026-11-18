"""Получение и вывод данных PokéAPI для обеих консольных практик."""

import re
from functools import lru_cache

from api_http import ApiNotFound, get_json

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"


def first_pokemon_names():
    """Вернуть имена первых двадцати покемонов в порядке API."""
    data = get_json(f"{BASE_URL}?limit=20&offset=0")
    return [pokemon["name"] for pokemon in data["results"]]


def find_pokemon(name):
    """Проверить имя и получить карточку покемона."""
    name = name.strip().lower()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name.isdecimal():
        raise ApiNotFound("Введите имя покемона из латинских букв, например clefairy.")
    try:
        return _get_pokemon(name)
    except ApiNotFound as error:
        raise ApiNotFound(f"Покемон «{name}» не найден.") from error


@lru_cache(maxsize=128)
def _get_pokemon(name):
    """Получить карточку по имени и сохранить её на время запуска."""
    return get_json(f"{BASE_URL}{name}/")


def print_pokemon(pokemon):
    """Вывести карточку, переведя дециметры и гектограммы в метры и килограммы."""
    types = ", ".join(item["type"]["name"] for item in pokemon["types"])
    abilities = ", ".join(item["ability"]["name"] for item in pokemon["abilities"])
    print(f"Имя: {pokemon['name']}")
    print(f"Типы: {types}")
    print(f"Вес: {pokemon['weight'] / 10:g} кг")
    print(f"Рост: {pokemon['height'] / 10:g} м")
    print(f"Способности: {abilities}")
