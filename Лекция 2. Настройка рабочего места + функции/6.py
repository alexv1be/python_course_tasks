# Задача #6 – виселица

import random


def get_hangman_stage(errors: int) -> str:
    """Возвращает графическое отображение виселицы в зависимости от ошибок."""
    stages = [
        "  \n  \n  \n  \n===",
        "  |\n  |\n  |\n  |\n===",
        "  |---- \n  |    \n  |    \n  |\n===",
        "  |----|\n  |    \n  |    \n  |\n===",
        "  |----|\n  |    O\n  |    \n  |\n===",
        "  |----|\n  |    O\n  |   /|\\\n  |\n===",
        "  |----|\n  |    O\n  |   /|\\\n  |   / \\\n==="
    ]
    return stages[errors]


def display_state(word: str, guessed: set, errors: int) -> str:
    """Выводит виселицу и текущее состояние отгадываемого слова."""
    print(get_hangman_stage(errors))

    # Генерация строки с угаданными буквами и пропусками
    display_word = "".join(char if char in guessed else "_" for char in word)

    print(f"Слово: {display_word}")
    print(f"Ошибок: {errors} из 6\n")
    return display_word


def play_hangman():
    """Основной цикл игры."""
    words = ["ПИТОН", "АЛГОРИТМ", "ФУНКЦИЯ", "КОМПИЛЯТОР", "РАЗРАБОТКА"]
    word = random.choice(words)
    guessed_letters = set()
    errors = 0
    max_errors = 6

    print("=== Добро пожаловать в игру 'Виселица' ===")

    while errors < max_errors:
        current_display = display_state(word, guessed_letters, errors)

        if "_" not in current_display:
            print("🎉 Поздравляю, вы угадали слово!")
            return

        guess = input("Введите букву: ").strip().upper()

        # Защита от некорректного ввода
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Пожалуйста, введите ровно одну русскую букву.")
            continue

        if guess in guessed_letters:
            print("⚠️ Вы уже вводили эту букву!")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            errors += 1

    # Если цикл закончился по лимиту ошибок
    print(get_hangman_stage(errors))
    print(f"💀 Вы проиграли! Загаданное слово было: {word}")


# Запуск игры
if __name__ == "__main__":
    play_hangman()