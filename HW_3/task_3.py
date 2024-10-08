# Дана строка s и символ k.
# Реализуйте функцию, рисующую рамку из символа k вокруг данной строки, например:
#
# **************
# *Текст в рамке*
# **************
def draw_text_frame(s: str, k: str):
    text = k + s + k
    len_text = len(text)
    print(len_text * k)
    print(text)
    print(len_text * k)

draw_text_frame('Пример текста','*')