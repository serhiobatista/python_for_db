# Даны n предложений. Определите, сколько из них содержат хотя бы одну цифру

def count_digit_in_sentences(*kwargs):
    list_int = ['0','1', '2','3','4','5','6','7','8','9']
    res = 0
    for sentence in kwargs:
        for digit in list_int:
            if digit in sentence:
                res += 1
                break
    return res


res = count_digit_in_sentences('Предложение 1,2,3','Предложение','Предложение 0,1')
print(res)
