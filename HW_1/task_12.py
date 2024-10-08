# Дано слово объектно-ориентированный.
# Используя индексацию и срезы составьте из него слова: объект, ориентир, тир, кот, рента и выведите их на экран.


template = 'объектно-ориентированный'

word_object = template[:6]
orientir = template[9:17]
tir = template[14:17]
kot = template[4] + template[7] + template[5]
renta = template[10] + template[12:15] + template[19]

for indx, val in enumerate(template):
    print(indx, val)

print(word_object, orientir, tir, kot, renta)
