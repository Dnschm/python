# Второе упражнение
input_list = list(input("Введите номера без пробела: "))
for i in range(1, len(input_list), 2):
    input_list[i - 1], input_list[i] = input_list[i], input_list[i - 1]

print(input_list)
