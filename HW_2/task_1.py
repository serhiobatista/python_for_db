a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
t = a.count(5)
print(t)
while t != 0:
    a.remove(5)
    t -= 1
a.extend(c)
t = a.count(3)
print(t)
print(a)