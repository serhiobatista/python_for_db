cnt_skates = int(input('Кол-во коньков: '))
skates_size = list()
for num in range(1, cnt_skates + 1):
    el = int(input('Размер {}-й пары: '.format(num)))
    skates_size.append(el)
skates_size = sorted(skates_size)

cnt_people = int(input('Кол-во людей: '))
foot_size = list()
for num in range(1, cnt_people + 1):
    el = int(input('Размер ноги {}-го человека: '.format(num)))
    foot_size.append(el)
foot_size = sorted(foot_size)

res = 0
for fs in range(len(foot_size)):
    for sz in range(len(skates_size)):
        if skates_size[sz] >= foot_size[fs]:
            del skates_size[sz]
            res += 1
            break
print('Наибольшее кол-во людей, которые могут взять ролики: {}'.format(res))

