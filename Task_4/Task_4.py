# Задача 1 «Длина отрезка» (1 балл)
m = input('Введите число: ').split(" ")
m[0] = int(m[0])
m[1] = int(m[1])
m[2] = int(m[2])
m[3] = int(m[3])
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2-y1)**2)**0.5
print(distance(m[0],m[1],m[2],m[3]))

# Задача 3 (1 балл)
stroka = input('Введите строку: ')
print(''.join([j for i,j in enumerate(stroka) if j not in stroka[:i]]))

# Задача 7 Кегельбан (2 балла)
import random
Kegl = int(input('Ввкдите колличесво кеглей: '))
Sh = int(input('Ввкдите колличесво шаров: '))
def Remove(s, l, r):
    i = l
    while i <= r:
        if s[i]:
            s[i] = "."
        i += 1
Skittles = []
for i in range(Kegl):
    Skittles.append("I")
for i in range(Sh):
    l = random.randint(0, Kegl - 1)
    r = random.randint(0, Kegl - 1)
    if l > r:
        l, r = r, l
    Remove(Skittles, l, r)
print("".join(Skittles))

# Задача 9 «Диагонали, параллельные главной» (1 балл)
def massiv(n):
    a = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            a[i][j] = abs(i - j)

    return a
for row in (massiv(7)):
    print(' '.join([str(elem) for elem in row]))

# Задача 10 Числа Фибоначчи (3 балла)
n = int(input('Введите число: '))
def fib(n):
    if n<3:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(20))
