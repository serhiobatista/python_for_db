v = float(input("Введите скорость (в км/ч): "))
t = float(input("Введите время (в часах): "))

distance = v * t
kilometer = int(distance % 123)
print("Спортсмен остановится на", kilometer, "километре")