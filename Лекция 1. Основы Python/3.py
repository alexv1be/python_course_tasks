# Задача #3: генератор паролей

import random
import string

letters = random.choices(string.ascii_uppercase, k=3)
numbers = random.choices(string.digits, k=3)
special_chars = random.choices('!@#$%^&*', k=3)

array = letters + numbers + special_chars
random.shuffle(array)
password = ''.join(array)
print(password)
