n = int(input())
seq = list()
for el in range(n):
    seq.append(int(input()))
cnt = 0
print('Последовательность:', seq)
while cnt < n - 1:
  length = (n - cnt) // 2
  if seq[cnt: cnt + length] == seq[: n - length - 1: -1]:
    break
  cnt += 1
print('Нужно приписать чисел:', cnt)
print('Сами числа:', seq[: cnt][:: -1])
