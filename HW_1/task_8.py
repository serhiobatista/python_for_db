first_num = int(input())
second_num = int(input())
third_num = int(input())

min_num = min(first_num, second_num, third_num)
max_num = max(first_num, second_num, third_num)
middle_num = first_num + second_num - third_num - min_num - max_num

print(min_num, middle_num, max_num)