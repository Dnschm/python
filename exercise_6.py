b = int(input("Какая желаемая скорость спортсмена?"))
a = int(input("Сколько спортсмен пробежал в первый день?"))
days = 1
if a == b:
    print("Спортсмен достиг своей цели уже на первый день")
else:
    while a < b:
        a = a * 1.1
        days = days + 1
    print(f"На {days} день скорость спортсмена стала больше, чем {b}")
