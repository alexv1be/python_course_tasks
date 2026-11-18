"""Практика № 1. Список покемонов и поиск карточки по имени."""

from api_http import ApiError
from pokemon_api import find_pokemon, first_pokemon_names, print_pokemon


def main():
    """Показать первые двадцать имён и запросить покемона у пользователя."""
    try:
        for number, name in enumerate(first_pokemon_names(), start=1):
            print(f"{number}. {name}")
        print_pokemon(find_pokemon(input("Имя покемона: ")))
    except ApiError as error:
        print(error)
    except (EOFError, KeyboardInterrupt):
        print("\nВыход.")


if __name__ == "__main__":
    main()
