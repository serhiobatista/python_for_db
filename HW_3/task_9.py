class NotationError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return 'NotationError, {0} '.format(self.message)
        else:
            return 'Указана некорекктная система счислеения'
def convert_to_ten_notation(num: int,
                            start_notation: int):
    power = 1
    ans = 0
    for el in str(num)[::-1]:
        if el < 'A':
            ans += int(el) * power
        else:
            ans += (ord(el) - ord('A') + 10) * power
        power *= start_notation
    return ans


def convert_notation(start_notation: int,
                     target_notation: int,
                     num: int):
    if (start_notation < 2 or start_notation > 16) or (target_notation < 2 or target_notation > 16):
        raise NotationError
    else:
        num_ten_notation = convert_to_ten_notation(num, start_notation)
        res = ''
        al = 'ABCDEF'
        while num_ten_notation > 0:
            remainder = num_ten_notation % target_notation
            if remainder < 10:
                res = str(remainder) + res
            else:
                res = al[remainder - 10] + res
            num_ten_notation //= target_notation
    return res

res = convert_notation(17, 3, 145)
print(res)
