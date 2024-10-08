# Строка называется палиндромом, если она пишется одинаково в обоих направлениях.
# Например, палиндромами в английском языке являются слова «anna», «civic», «level», «hannah».
# Напишите программу, запрашивающую у пользователя строку и при помощи цикла определяющую, является ли она палиндромом.

def is_palindrome(word: str) -> bool:
    iters = len(word) // 2
    for i in range(iters):
        if word[i] != word[-i - 1]:
            return False
    return True

test1 = is_palindrome('anna')
print(test1)

test2 = is_palindrome('python')
print(test2)

test3 = is_palindrome('hannah')
print(test3)



