# Магическими называются даты, в которых произведение дня и месяца составляет последние две цифры года.
# Например, 10 июня 1960 года – магическая дата, поскольку 10 ´ 6 = 60.
# Напишите функцию, определяющую, является ли введенная дата магической.
# Используйте написанную функцию в главной программе для отображения всех магических дат в XX веке.
import datetime


def is_magic(date: str) -> bool:
    day_splitted = date.split('.')
    if int(day_splitted[0]) * int(day_splitted[1]) ==  int(day_splitted[2]) % 100:
        return True
    else:
        return False


start_date = datetime.datetime(1901, 1, 1)
all_dates = [start_date + datetime.timedelta(days=idx) for idx in range(36525)]

magic_dates = list()
for idx in range(len(all_dates)):
    dt = all_dates[idx].strftime('%d.%m.%Y')
    if is_magic(dt):
        magic_dates.append(dt)
print(magic_dates)



