# Первое упражнение
random_list = [1, 5.5, -2, "Random text", True]
x = dict()

for n in range(len(random_list)):
    x[n] = type(random_list[n])
print(x)
