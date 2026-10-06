# Задача #4: анализ текста

string = input("Введите строку: ").lower()

counts = {}
for char in string:
    counts[char] = counts.get(char, 0) + 1

top_three = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:3]

print("3 самых частых символа:")
for char, count in top_three:
    print(f"Символ '{char}' встречается {count} раз(а)")