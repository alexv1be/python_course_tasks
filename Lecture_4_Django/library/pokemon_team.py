"""Практика № 3. Консольный менеджер команды покемонов."""

from api_http import ApiError
from pokemon_api import find_pokemon, print_pokemon


def battle_score(pokemon):
    """Посчитать сумму базовых характеристик для тренировочного боя."""
    return sum(stat["base_stat"] for stat in pokemon["stats"])


def train(team, first_name, second_name):
    """Провести упрощённый бой между двумя разными участниками команды."""
    if first_name == second_name:
        print("Выберите двух разных покемонов.")
        return
    if first_name not in team or second_name not in team:
        print("Оба покемона должны быть в команде.")
        return

    first_score = battle_score(team[first_name])
    second_score = battle_score(team[second_name])
    print(f"{first_name}: {first_score}, {second_name}: {second_score}")
    if first_score == second_score:
        print("Ничья.")
    else:
        winner = first_name if first_score > second_score else second_name
        print(f"Победитель: {winner}")


def add_pokemon(team, name):
    """Добавить покемона по имени, исключая дубликаты."""
    if name in team:
        print(f"{name} уже в команде.")
        return
    pokemon = find_pokemon(name)
    canonical_name = pokemon["name"]
    if canonical_name in team:
        print(f"{canonical_name} уже в команде.")
        return
    team[canonical_name] = pokemon
    print(f"{canonical_name} добавлен в команду.")


def remove_pokemon(team, name):
    """Удалить покемона по имени или сообщить, что его нет в команде."""
    if team.pop(name, None) is None:
        print(f"{name} отсутствует в команде.")
    else:
        print(f"{name} удалён из команды.")


def show_team(team):
    """Вывести карточки и характеристики всех участников команды."""
    if not team:
        print("Команда пока пуста.")
    for pokemon in team.values():
        print()
        print_pokemon(pokemon)
        for stat in pokemon["stats"]:
            print(f"  {stat['stat']['name']}: {stat['base_stat']}")


def ask_name(prompt="Имя покемона: "):
    """Прочитать имя и привести его к формату PokéAPI."""
    return input(prompt).strip().lower()


def main():
    """Обработать команды пользователя до выхода из программы."""
    team = {}
    while True:
        print(
            "\n1. Добавить   2. Удалить   3. Показать команду\n"
            "4. Найти по имени   5. Тренировочный бой   0. Выйти"
        )
        try:
            command = input("Действие: ").strip()
            match command:
                case "1":
                    add_pokemon(team, ask_name())
                case "2":
                    remove_pokemon(team, ask_name())
                case "3":
                    show_team(team)
                case "4":
                    print_pokemon(find_pokemon(ask_name()))
                case "5":
                    if len(team) < 2:
                        print("Для боя добавьте в команду хотя бы двух покемонов.")
                        continue
                    train(team, ask_name("Первый покемон: "), ask_name("Второй покемон: "))
                case "0":
                    return
                case _:
                    print("Выберите действие из меню.")
        except ApiError as error:
            print(error)
        except (EOFError, KeyboardInterrupt):
            print("\nВыход.")
            return


if __name__ == "__main__":
    main()
