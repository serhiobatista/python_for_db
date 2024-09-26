# Дано двузначное и трехзначное число. Для каждого выведите на экран сумму и произведение цифр.

two_digit_num, three_digit_num = input(), input()
sum_two_digit_num = int(two_digit_num[0]) + int(two_digit_num[1])
sum_three_digit_num = int(three_digit_num[0]) + int(three_digit_num[1]) + int(three_digit_num[2])

print(sum_two_digit_num, sum_three_digit_num)

