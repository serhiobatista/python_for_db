N = int(input('Кол-во человек: '))
K = int(input('Число: '))
print('Значит, выбывает каждый', K, '-й человек')
people = list(range(1, N + 1))

out = 0
while len(people) > 1:
    print('Текущий круг людей', people)
    start_count = out % len(people)
    out = (start_count + K - 1) % len(people)
    print('Начало счёта с номера', people[start_count])
    print('Выбывает человек под номером', people[out])
    people.remove(people[out])
    print()

last_person = people[0]
print('Остался человек под номером', last_person)