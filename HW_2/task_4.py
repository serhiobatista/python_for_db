guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
cnt_guests = len(guests)

stop_words = 'Вечеринка закончилась, все легли спать.'
while True:
    print('Сейчас на вечеринке {} человек: {}'.format(cnt_guests, guests))
    action = input('Гость пришёл или ушёл? ')
    if action == stop_words:
        break
    guest_name = input('Имя гостя: ')
    if action.lower() == 'пришел' or action.lower() == 'пришёл':
        if cnt_guests == 5:
            print('Прости, {}, но мест нет.'.format(guest_name))
        else:
            guests.append(guest_name)
            cnt_guests += 1
            print('Привет, {} !'.format(guest_name))
    elif action.lower() == 'ушел' or action.lower() == 'ушёл':
        guests.remove(guest_name)
        cnt_guests -= 1
        print('Пока {} !'.format(guest_name))
print('Вечеринка закончилась, все легли спать.')
