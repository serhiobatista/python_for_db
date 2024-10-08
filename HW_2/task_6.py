first_list = list()
for num in range(1,4):
    el = int(input('Введите {}-е число для первого списка: '.format(num)))
    first_list.append(el)
second_list = list()
for num in range(1,8):
    el = int(input('Введите {}-е число для второго списка: '.format(num)))
    second_list.append(el)
print('Первый список: {}'.format(first_list))
print('Второй список: {}'.format(second_list))
first_list.extend(second_list)
print('Новый первый список с уникальными элементами: {}'.format(list(set(first_list))))
