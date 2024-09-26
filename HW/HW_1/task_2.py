# Составьте программу, которая запрашивает у пользователя 2 целых числа и выполняет операции:
# арифметические: +, -, * , / , // , %, **, log10;
# сравнение: <, <=, >, >=, !=, ==,
# выводя на экран результат каждого действия. В случае получение вещественного результата, округлите его до 2-х знаков после запятой (используя функцию round()).
# Подсказка. Функцию log10 вы найдете в модуле math.

import math as m
first_num, second_num = int(input()), int(input())

summing = first_num + second_num
minus = first_num - second_num
multiply = first_num * second_num
divide = first_num / second_num
divide_whole_part = first_num // second_num
divide_remainder = first_num % second_num
degree = first_num ** second_num
log_first, log_second = m.log10(first_num),  m.log10(second_num)

print(summing, minus, multiply, round(divide,2),
      round(divide_whole_part, 2), round(divide_remainder, 2),
      degree, round(log_first, 2), round(log_second, 2))

is_less = first_num < second_num
is_less_or_eq = first_num <= second_num
is_greater = first_num > second_num
is_greater_or_eq = first_num >= second_num
is_not_eq = first_num != second_num
is_eq = first_num == second_num

print(is_less, is_less_or_eq, is_greater, is_greater_or_eq, is_not_eq, is_eq)





