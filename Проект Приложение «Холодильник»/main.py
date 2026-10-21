from decimal import Decimal
from datetime import datetime, date, timedelta


DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []

    if expiration_date is not None:
        expiration_date = datetime.strptime(str(expiration_date), DATE_FORMAT).date()

    items[title].append({'amount': amount, 'expiration_date': expiration_date})


def is_date_simple(date_string):
    return len(date_string) == 10 and date_string.replace('-', '').isdigit()


def add_by_note(items, note):
    expiration_date = None
    parts = note.split()

    if is_date_simple(parts[-1]):
        expiration_date = datetime.strptime(parts.pop(), DATE_FORMAT).date()
    amount = Decimal(parts.pop())
    title = ' '.join(parts)

    add(items, title, amount, expiration_date)


def find(items, needle):
    matching_items = []
    for key in items.keys():
        if needle.lower() in key.lower():
            matching_items.append(key)
    return matching_items


def get_amount(items, needle):
    amount = Decimal('0')
    for key in find(items, needle):
        for batch in items[key]:
            amount += batch['amount']
    return amount

def get_expired(items, in_advance_days=0):
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
