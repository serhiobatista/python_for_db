# Используя шифр Цезаря (достаточно только букв русского алфавита, знаки препинания не изменяются),
# зашифруйте, а затем расшифруйте введенную строку.

def encrypt_caesar(txt,
                  shift = 3,
                  special_chars = [',', '.', ';', ' ', '!', '?'],
                   rus_alhabet= 'абвгдежзийклмнопрстуфхцчшщъыьэюя'):
    res = ''
    for idx in range(0, len(txt)):
        char = txt[idx]
        if char in special_chars:
            res += char
        elif char.isupper():
            idx = rus_alhabet.find(char.lower()) + 1
            idx_caesar = (idx + shift) % 33
            res += rus_alhabet[idx_caesar + 1].upper()
        else:
            idx = rus_alhabet.find(char) + 1
            idx_caesar = (idx + shift)
            res += rus_alhabet[idx_caesar + 1]
    return res

result = encrypt_caesar('Это текстовое сообщение.')
print(result)