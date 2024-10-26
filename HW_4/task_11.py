num_dict = {5: 'A', 4: ('B', 'C'), 3: ('B', 'E'), 2: 'P'}
symbol_dict = {'A': 5, 'B': (4, 3), 'C': 4, 'E': 3, 'P': 2}
while True:
    try:
        grade = input('Введите оценку: ')
        if grade == '':
            break
        print(num_dict[int(grade)])
    except (KeyError, ValueError) as err:
        print('Не удалось сконвертировать численную оценку в буквенную. Делаю обратную операцию.')

    try:
        print(symbol_dict[grade.upper()])
    except (KeyError, ValueError) as err:
        print('Введенное значение не является допустимым.')



