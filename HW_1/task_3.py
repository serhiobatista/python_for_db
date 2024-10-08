# Вычислите значение следующего выражения (аргументы - целые числа и вводятся с клавиатуры):
# f = 3x5 + 7|-6|  y7 - z mody
# Округлите результат до 3-х знаков после запятой, используя функцию round().

import math as m
x, y, z = int(input()), int(input()), int(input())

arg_1 = ((m.pow(x, 5) + 7) / (abs(-6) * y)) **(1/3)
arg_2 = 7 - z * abs(y)
res = arg_1 / arg_2
print(round(res, 3))
