# Задача #5 – римский конвертер

def roman_to_int(roman: str) -> int:
    """Конвертирует римские цифры в обычные целые числа."""
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    # Идем с конца строки, чтобы легко вычитать меньшие числа (например, I в IV)
    for char in reversed(roman):
        value = roman_map[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total


def int_to_roman(num: int) -> str:
    """Конвертирует обычные целые числа в римские цифры."""
    val_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ""

    for val, sym in val_map:
        while num >= val:
            result += sym
            num -= val

    return result


# Блок тестирования программы
if __name__ == "__main__":
    roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]

    print("--- Из римских в обычные и обратно ---")
    for roman_num in roman_tests:
        # 1. Переводим в обычное число
        normal_num = roman_to_int(roman_num)

        # 2. Переводим обратно в римское для проверки
        reverted_roman = int_to_roman(normal_num)

        print(f"Римское: {roman_num:7} -> Арабское: {normal_num:4} -> Обратно: {reverted_roman}")