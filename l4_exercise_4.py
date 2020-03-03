# Четвертое упражнение
string = input("Введите строки с пробелами: ").split()
for i, word in enumerate(string, 1):
    print(f"{i} {word[:10]}")


