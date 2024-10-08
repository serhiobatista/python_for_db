equation = input('Введите уравнение вида: ax+b=0: ')
limits = list(map(int, input('Введите нижнюю и верхнюю границу отрезка через запятую: ').split(',')))
a = int(equation.split('x')[0])
b = int(equation.split('+')[1].split('=')[0])
res = -b/a
if limits[0] <= res <= limits[1]:
    print('Решение уравнения попадает в указанный отрезок.')
else:
    print('Решение уравнения не попадает в указанный отрезок.')
