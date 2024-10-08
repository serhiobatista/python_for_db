N = int(input('Кол-во друзей: '))
K = int(input('Долговых расписок: '))

debt_papers = list()
for num in range(1, K + 1):
    debt_paper = list()
    print('{}-я расписка'.format(num))
    whom = int(input('Кому: '))
    debt_paper.append(whom)
    who = int(input('От кого: '))
    debt_paper.append(who)
    how_much = int(input('Сколько: '))
    debt_paper.append(how_much)
    debt_papers.append(debt_paper)

balance = dict()
for key in range(1, N + 1):
    balance[key] = 0
print(balance)

for debt_paper in debt_papers:
    balance[debt_paper[1]] += debt_paper[2]
    balance[debt_paper[0]] -= debt_paper[2]
print('Баланс друзей {}'.format(balance))
