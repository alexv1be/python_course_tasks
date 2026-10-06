# Задача #6: ряд натуральных чисел

n = int(input())

length = 1
count = 9
start = 1

while n > length * count:
    n -= length * count
    length += 1
    count *= 10
    start *= 10

actual_number = start + (n - 1) // length
digit_index = (n - 1) % length

print(str(actual_number)[digit_index])
