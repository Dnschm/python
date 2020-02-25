revenue = int(input("Введите выручку фирмы (в у.е): "))  # Пользователь вводит выручку
cost = int(input("Введите издержки фирмы (в у.е): "))  # Пользователь вводит издержки
if revenue > cost:
    profit = revenue - cost
    print(f"Прибыль фирмы составила {profit} у.е")
    rate = int(profit / revenue * 100)
    print(f"Рентабельность фирмы равна {rate} %")
    people = int(input("Сколько сотрудников в фирме? "))
    ratio_to_people = profit / people
    print(f"Прибыль в расчете на одного сотрудника равна {int(ratio_to_people)} у.е")
if revenue < cost:
    loss = cost - revenue
    print(f"Убыток фирмы составил {loss} у.е ")
if revenue == cost:
    print("Выручка фирмы равна издержкам")
