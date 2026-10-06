# Задача #1 – шифр Цезаря

def detect_language(text: str) -> str:
    """Определяет язык входного текста по кодам символов."""
    ru_count = 0
    en_count = 0

    for char in text:
        code = ord(char)
        # Коды русского алфавита (А-Я, а-я) + Ё/ё
        if (1040 <= code <= 1103) or code in (1025, 1105):
            ru_count += 1
        # Коды английского алфавита (A-Z, a-z)
        elif (65 <= code <= 90) or (97 <= code <= 122):
            en_count += 1

    if ru_count >= en_count and ru_count > 0:
        return "Русский"
    elif en_count > ru_count:
        return "Английский"
    return "Неизвестный язык или только спецсимволы"

def shift_character(char: str, shift: int) -> str:
    """Сдвигает символ, используя его числовой код (ASCII/Unicode)."""
    code = ord(char)

    # Английский нижний регистр (a-z: 97-122)
    if 97 <= code <= 122:
        return chr((code - 97 + shift) % 26 + 97)
    # Английский верхний регистр (A-Z: 65-90)
    elif 65 <= code <= 90:
        return chr((code - 65 + shift) % 26 + 65)

    # Обработка 'Ё' и 'ё' (приводим к 'Е' и 'е')
    if code == 1105: code = 1077 # 'ё' -> 'е'
    elif code == 1025: code = 1045 # 'Ё' -> 'Е'

    # Русский нижний регистр (а-я: 1072-1103)
    if 1072 <= code <= 1103:
        return chr((code - 1072 + shift) % 32 + 1072)
    # Русский верхний регистр (А-Я: 1040-1071)
    elif 1040 <= code <= 1071:
        return chr((code - 1040 + shift) % 32 + 1040)

    return char # Спецсимволы и пробелы возвращаем как есть

def caesar_cipher(text: str, shift: int, mode: str = "encrypt") -> str:
    """Шифрует или дешифрует текст."""
    if mode == "decrypt":
        shift = -shift

    result = ""
    for char in text:
        result += shift_character(char, shift)

    return result

# Блок тестирования программы
if __name__ == "__main__":
    test_texts = [
        "Привет, мир! Это тест.",
        "Hello, World! This is a test."
    ]

    for original_text in test_texts:
        print("-" * 40)
        print(f"Оригинал: {original_text}")
        print(f"Определен язык: {detect_language(original_text)}")

        encrypted = caesar_cipher(original_text, 3, mode="encrypt")
        print(f"Зашифровано: {encrypted}")

        decrypted = caesar_cipher(encrypted, 3, mode="decrypt")
        print(f"Расшифровано: {decrypted}")