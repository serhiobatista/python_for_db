exit_symbol = ''
total = 0
curr_num = None
while True:
    try:
        curr_num = input('Введите число: ')
        if curr_num == exit_symbol:
            break
        total += float(curr_num)
        print(total)
    except ValueError:
        print('Ввод в некорректном формате, попробуйте еще раз.')
print(f'Итоговая сумма: {total}')
