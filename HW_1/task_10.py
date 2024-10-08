# Составьте программу, которая запрашивает название футбольной команды и повторяет его на экране со словами
# ... - чемпион!
#
# После этого выполните:
# используя операцию дублирования, нарисуйте черту (набор "-"), длиной, равной размеру названия команды;
# преобразуйте строку в нижний регистр и выведите на экран:
# длину наименования команды;
# есть ли в наименовании команды буква "п" (True/False)?
# сколько раз повторяется буква "а"?

football_team = input()
print('{} - чемпион!'.format(football_team))
print('-' * len(football_team))
football_team_lower = football_team.lower()
print('Длина наименования команды - {} '.format(football_team_lower))
is_p_in_name = 'п' in football_team_lower
print('Есть ли буква "п" в названии команды: {}'.format(is_p_in_name))
print('Буква "а" повторяется в строке {} раз'.format(football_team_lower.count('а')))
