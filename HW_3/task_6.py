# Напишите функцию, которая принимает неограниченное количество числовых аргументов и возвращает кортеж из двух списков:
# отрицательных значений (отсортирован по убыванию);
# неотрицательных значений (отсортирован по возрастанию).

def create_number_list(*kwargs):
    negative_nums = list()
    positive_nums = list()
    for el in kwargs:
        if not isinstance(el, (int, float)):
            continue
        elif el < 0:
            negative_nums.append(el)
        else:
            positive_nums.append(el)
    negative_nums_sorted = sorted(negative_nums, reverse=True)
    positive_nums_sorted = sorted(positive_nums)
    return negative_nums_sorted, positive_nums_sorted


res_tuple = create_number_list(2,5,6,7,0,-19,-2,-100)
print(res_tuple)

