import random
n = int(input("Ширина матрицы"))
m = int(input("Высота матрицы"))
k = int(input(f"Строка матрицы (<{n})"))
p = int(input(f"Столбец матрицы (<{m})"))
r = int(input("Эллемент строки матрицы"))
t = int(input("Эллемент столбца матрицы"))
a = []
mat = [[random.randint(1,9) for i in range(n)] for b in range(m)]
i = 0
for b in mat:
    print(b)
for b in mat:
    a.append(mat[i][i])
    i+=1
print(f"Диагональ {a}")
print(mat[k-1])
b = [i[p-1] for i in mat]
print(b)
print(mat[r-1][t-1])

