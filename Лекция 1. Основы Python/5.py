# Задача #5: поиск простых чисел

n = int(input())

is_prime = [True] * (n + 1)
primes = []

for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)

print(*primes)
