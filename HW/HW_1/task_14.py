# Создайте пустой словарь для хранения информации о себе и выполните операции, описанные в заготовке.
# В данной задаче все значения задаются в коде (без input())

# 1. Создание словаря
# Создать пустой словарь
info = {}

# Добавить значения для ключей "фио", "дата_рождения", "место_рождения"
info["фио"] = 'Колесов Сергей Владимирович'
info['дата_рождения'] = '01.09.1998'
info['место_рождения'] = 'г. Воркута'

# Напечатать словарь
print(info)

info['хобби'] = ['плавание', 'бег', 'стрельба по уткам']
info['хобби'].append('программирование')

info['животные'] = ('кошка Мурка', 'собака Фунтик', 'попугай Кеша')
info['ЕГЭ'] = {}

info['ЕГЭ']['математика'] = 100
info['ЕГЭ']['русский язык'] = 100

info['ЕГЭ']['литература'] = 10
del info['ЕГЭ']['литература']


info['вузы'] = {}
info['вузы']['МГУ'] = 210
info['вузы']['СГУ'] = 220

# 2. Вывод на экран
print("Данные:")
print(info)


# Список экзаменов ЕГЭ в алфавитном порядке
# (используйте метод ``keys()``, преобразовав результат в кортеж)
exams = tuple(sorted(info['ЕГЭ'].keys()))
print("Предметы:", exams)
# Список вузов в алфавитном порядке
uni = tuple(sorted(info['вузы'].keys()))
print("Вузы:", uni)


# 3. Ответы на вопросы
print("\nОтветы на вопросы:")

# Выделить имя из info["фио"]
name = info['фио'].split(' ')[1]
# Начинается на гласную? (True/False)
starts_with_vowel = name[0] in ['А','Е', 'Ё', 'О', 'У', 'Э', 'Я', 'Ю', 'И']
print("* мое имя начинается на гласную букву:", starts_with_vowel)

month = int(info['дата_рождения'].split('.')[1][1]) if info['дата_рождения'].split('.')[1][0] == '0' else int(info['дата_рождения'].split('.')[1])
born_in_winter_or_summer = month in (12,1,2,6,7,8)
print("* родился летом или зимой: {}".format(born_in_winter_or_summer))

# Количество хобби и первое из них
hobbies_count = len(info['хобби'])
print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, info['хобби'][0]))

# Количество сданных экзаменов
print("* после окончания школы сдавал {} экз.".format(len(info['ЕГЭ'])))

# Сумма баллов по экзаменам
sum_mark = sum(info['ЕГЭ'].values())
print("* сумма баллов = {}".format(sum_mark))

# Максимальный балл среди сданных
max_mark = max(info['ЕГЭ'].values())
print("* макс. балл = {}".format(max_mark))

# Количество вузов, в которые Вы проходите по баллам
# Подсказка: определить, проходите Вы или нет, можно простым сравнением
# суммы баллов с проходным баллом вуза - ``True/False``.
# Для того, чтобы определить количество таких вузов, преобразуйте
# сравнение в целое число (используя ``int()``) и сложите все сравниваемые вузы.
is_enrolled_msu = sum_mark >= info['вузы']['МГУ']
is_enrolled_ssu = sum_mark >= info['вузы']['СГУ']
vuz_count = is_enrolled_msu + is_enrolled_ssu
print("* кол-во вузов в которые прохожу: {}".format(vuz_count))