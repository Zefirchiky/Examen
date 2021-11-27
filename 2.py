import random
a = []
n = int(input("Количество эллементов списка:"))
b = 1
for i in range(n):
    a.append(random.randint(0,15))
for i in a:
    b*=i
print(f"Первый {a[0]}")
print(f"Последний {a[-1]}")
print(f"Призведение {b}")
