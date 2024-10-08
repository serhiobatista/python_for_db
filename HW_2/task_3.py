shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail_name = input('Введите название детали: ')
counter = 0
total_sum = 0
for num_list in range(len(shop)):
    if shop[num_list][0] == detail_name:
        counter += 1
        total_sum += shop[num_list][1]
print('Кол-во деталей — {}'.format(counter))
print('Общая стоимость — {}'.format(total_sum))