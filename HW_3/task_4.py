# Для введенного предложения выведите статистику символ=количество. Регистр букв не учитывается.

def count_symbols(sentence: str):
    res = dict()
    lowered_sentence = sentence.lower()
    for symbol in lowered_sentence:
        if symbol in res:
            res[symbol] += 1
        else:
            res[symbol] = 0
    return res

res = count_symbols('Тестовое предложение для проверки функции.')
print(res)
