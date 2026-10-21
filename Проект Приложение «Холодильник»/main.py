from datetime import date, datetime, timedelta
from decimal import Decimal

# Формат строкового представления дат, принятый в ТЗ (ГГГГ-ММ-ДД).
DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    """
    Добавляет партию продукта в словарь хранилища.

    Если товар добавляется впервые, создаёт для него новый список партий.
    Преобразует строковую дату годности в объект datetime.date.

    :param items: Словарь хранилища (goods).
    :param title: Название продукта (ключ словаря).
    :param amount: Количество продукта в партии (Decimal).
    :param expiration_date: Срок годности в формате DATE_FORMAT (опционально).
    """
    if title not in items:
        items[title] = []

    if expiration_date is not None:
        expiration_date = datetime.strptime(str(expiration_date), DATE_FORMAT).date()

    items[title].append({'amount': amount, 'expiration_date': expiration_date})


def is_date_simple(date_string):
    """
    Вспомогательная валидация шаблона YYYY-MM-DD для отделения
    даты от количества при разборе текстовой строки.
    """
    return len(date_string) == 10 and date_string.replace('-', '').isdigit()


def add_by_note(items, note):
    """
    Парсит произвольную текстовую строку и добавляет партию через add().

    Ожидаемый формат строки: "<название> <количество> [срок годности]".
    Поскольку название может состоять из нескольких слов с пробелами,
    разбор структуры выполняется с конца строки:
    - последний элемент проверяется на дату;
    - предпоследний (или последний, если даты нет) принимается за количество;
    - оставшаяся левая часть собирается обратно в единое название товара.

    :param items: Словарь хранилища (goods).
    :param note: Строка с описанием закупки.
    """
    expiration_date = None
    parts = note.split()

    # Извлечение опционального срока годности с конца строки
    if is_date_simple(parts[-1]):
        expiration_date = datetime.strptime(parts.pop(), DATE_FORMAT).date()

    amount = Decimal(parts.pop())
    title = ' '.join(parts)

    add(items, title, amount, expiration_date)


def find(items, needle):
    """
    Выполняет регистронезависимый поиск продуктов по подстроке.

    :param items: Словарь хранилища (goods).
    :param needle: Искомая подстрока.
    :return: Список названий продуктов, содержащих подстроку needle.
    """
    matching_items = []
    for key in items.keys():
        if needle.lower() in key.lower():
            matching_items.append(key)
    return matching_items


def get_amount(items, needle):
    """
    Подсчитывает суммарное количество продукта по всем его партиям,
    названия которых частично или полностью совпадают с поисковой строкой.

    :param items: Словарь хранилища (goods).
    :param needle: Подстрока для поиска продуктов через find().
    :return: Общий объем/вес найденных продуктов типом Decimal.
    """
    amount = Decimal('0')
    for key in find(items, needle):
        for batch in items[key]:
            amount += batch['amount']
    return amount


def get_expired(items, in_advance_days=0):
    """
    Определяет просроченные продукты и партии с истекающим сроком годности.

    Фильтрует партии с условием: expiration_date <= (today + in_advance_days).
    Партии со значением expiration_date=None игнорируются (бессрочные).

    :param items: Словарь хранилища (goods).
    :param in_advance_days: Число дней вперёд от текущей даты для включения
                            в выборку скоропортящихся остатков (по умолчанию 0).
    :return: Список кортежей вида [(title, expired_amount), ...]
             только для тех товаров, у которых просроченный остаток строго > 0.
    """
    # Граничная дата контроля годности
    period = date.today() + timedelta(days=in_advance_days)
    expired_products = []

    for title, batches in items.items():
        expired_amount = Decimal('0')

        for batch in batches:
            if batch['expiration_date'] is not None and batch['expiration_date'] <= period:
                expired_amount += batch['amount']

        if expired_amount > 0:
            expired_products.append((title, expired_amount))

    return expired_products


if __name__ == '__main__':
    # Инициализация пустого холодильника
    goods = {}

    # 1. Добавление продуктов напрямую через add()
    add(goods, 'Пельмени Универсальные', Decimal('0.5'), '2026-11-15')
    add(goods, 'Пельмени Универсальные', Decimal('2'), '2026-12-01')
    add(goods, 'Вода', Decimal('1.5'))

    # 2. Добавление продуктов через текстовые заметки add_by_note()
    add_by_note(goods, 'Яйца куриные 10 2026-10-25')
    add_by_note(goods, 'Яйца перепелиные 20')
    add_by_note(goods, 'Масло сливочное 82.5% 0.2 2026-10-20')

    print('--- Текущее содержимое холодильника ---')
    for item_name, batches in goods.items():
        print(f'{item_name}: {batches}')

    print('\n--- Поиск продуктов (needle="яйца") ---')
    found_items = find(goods, 'яйца')
    print(f'Найдено: {found_items}')

    print('\n--- Подсчёт суммарного количества ---')
    total_eggs = get_amount(goods, 'яйца')
    print(f'Всего яиц: {total_eggs}')

    print('\n--- Проверка просроченных продуктов (на 2 дня вперёд) ---')
    expiring_soon = get_expired(goods, in_advance_days=2)
    print(f'Истекает срок годности: {expiring_soon}')