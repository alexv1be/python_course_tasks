# Задача #1-4: "calculator"

import numpy as np


def add_numbers(a: float, b: float) -> float:
    """Рассчитывает сумму двух чисел.

    Args:
        a (float): Первое слагаемое.
        b (float): Второе слагаемое.

    Returns:
        float: Результат сложения.
    """
    return a + b


def divide(a: float, b: float) -> float:
    """Выполняет деление первого числа на второе с защитой от нуля.

    Args:
        a (float): Делимое.
        b (float): Делитель.

    Returns:
        float: Результат деления.

    Raises:
        ValueError: Если делитель равен нулю.
    """
    # Иисправление задачи #4: Добавлена проверка деления на 0, чтобы код не падал
    if b == 0:
        raise ValueError("Деление на ноль невозможно.")
    return a / b


# Тестирование и проверка работы
if __name__ == "__main__":
    # Проверка использования numpy из задачи #1
    test_array = np.array([1.0, 2.0, 3.0])

    # Тест функции сложения из задачи #3
    sum_result = add_numbers(10.5, 4.5)
    print(f"Тест сложения (10.5 + 4.5): {sum_result}")
    assert sum_result == 15.0, "Ошибка в тесте сложения!"

    # Тест исправленной функции деления из задачи #4
    try:
        div_result = divide(10.0, 2.0)
        print(f"Тест деления (10.0 / 2.0): {div_result}")

        # Проверяем защиту от нуля
        divide(5.0, 0.0)
    except ValueError as e:
        print(f"Защита деления на ноль сработала успешно: {e}")
