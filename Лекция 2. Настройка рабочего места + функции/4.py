# Задача #4 – сложные пароли

import random
import string


def get_boolean_input(prompt: str) -> bool:
    """Запрашивает у пользователя ответ 'да' или 'нет'."""
    while True:
        answer = input(f"{prompt} (д/н): ").strip().lower()
        if answer in ('д', 'да', 'y', 'yes'):
            return True
        if answer in ('н', 'нет', 'n', 'no'):
            return False
        print("  -> Пожалуйста, введите 'д' (да) или 'н' (нет).")


def generate_password(length: int, use_lower: bool, use_upper: bool,
                      use_digits: bool, use_spec: bool) -> str:
    """Генерирует пароль на основе выбранных настроек."""
    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_spec:
        chars += "!@#$%^&*"

    if not chars:
        return "Ошибка: не выбрано ни одного типа символов!"

    return "".join(random.choice(chars) for _ in range(length))


def run_password_generator():
    """Запускает красивый интерфейс терминала."""
    print("=" * 45)
    print(" -*-  ГЕНЕРАТОР СЛОЖНЫХ ПАРОЛЕЙ  -*- ")
    print("=" * 45)

    try:
        length_input = input("\n1. Введите длину пароля (например, 12): ")
        length = int(length_input)
        if length <= 0:
            print("Ошибка: длина должна быть положительным числом.")
            return
    except ValueError:
        print("Ошибка: необходимо ввести целое число.")
        return

    print("\n--- Настройки символов ---")
    use_lower = get_boolean_input("2. Использовать строчные буквы (a-z)?")
    use_upper = get_boolean_input("3. Использовать прописные буквы (A-Z)?")
    use_digits = get_boolean_input("4. Использовать цифры (0-9)?")
    use_spec = get_boolean_input("5. Использовать спецсимволы (!@#$%^&*)?")

    password = generate_password(length, use_lower, use_upper, use_digits, use_spec)

    print("\n" + "=" * 45)
    print(" ВАШ СГЕНЕРИРОВАННЫЙ ПАРОЛЬ:")
    print(f" >  {password}  <")
    print("=" * 45 + "\n")


# ==========================================
# Запуск программы
# ==========================================
if __name__ == "__main__":
    run_password_generator()