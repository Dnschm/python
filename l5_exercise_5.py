# Пятое упражнение
some_list = [1,2,3,4,5]
input_number = int(input("Введите новое число: "))
i = 0
for n in some_list:
    if input_number <= n:
        i = i + 1
some_list.insert(i, input_number)
print(some_list)

