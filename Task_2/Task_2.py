# #Задача 1 Приветствие (1 балл)
# Напишите программу, которая запрашивает имя пользователя, а затем приветствует его.
#
name=input('Введите ваше имя: ')
print('Привет, '+name+'!')

# # Задача 2 Возведение в степень. (1 балл)
# # Вычислите $2^{20}$. Выведите на экран вычисленное значение.
chislo = 2**20
print(chislo)

# Задача 3 Гипотенуза (1 балл)

katet_1 = int(input('Введите первый катет: '))
katet_2 = int(input('Введите второй катет: '))
sum_kat = katet_1**2+katet_2**2
print(sum_kat**0.5)

# Задача 4 Делёж яблок (1 балл)

student = int(input('Количество школьников: '))
appels = int(input('Количество яблок: '))
print(appels//student)

# Задача 5 (1 балл)
# Напишите программу, которая считывает целое число и выводит текст, указанный ниже, который содеражит следующее и предыдущее числа.
# Сохраните пробелы и переносы строк, указанные в тексте.
number = int(input('Введите число: '))
plus = number+1
minos = number-1
print('Получено число -'+str(number)+'. \nСледующие число -'+str(plus)+', предыдущее число -'+str(minos)+'.')

# Задача 6 (1.5 балла)

rundom_number = int(input('Введи целое число: '))
print(rundom_number+2-(rundom_number%2))

# Задача 7 (1.5 балла)

big_number = list(input('Введите числа: '))
for key, value in enumerate(big_number):
    big_number[key] = int(value)

print(sum(big_number))

# Задача 9 (1 балл)
# Как и в прошлом задании пользователь подает на вход список. Вам нужно вывести все элементы списка, стоящие на четных индексах.
spisok = list(input('Введите числа: '))
print(spisok[::2])

# Задача 10 (1 балл)
# Пользователь поочередно вводит 2 целых числа $n$ и $m$, при чем $n \le m$. Выведите все числа от $n$ до $m$ включительно. Обратите внимаие на формат вывода!
n = int(input('Введите число m:'))
m = int(input('Введите число больше, чем n:'))
for i in range(n,m+1):
     print (i)

# Задача 11 Ряд Лейбница (2 балла)
res = 0
for i in range(100):
    res += 4 * ((-1)**i) / (2 * i + 1)

print(res)
#
# #Задача 12 (1 балл)

n = int(input('Введите число: '))
l = list(range(1, n + 1))
print(l)
for i in range(0, len(l) - 1, 2):
    l[i], l[i+1] = l[i+1], l[i]
print(l)

# Задача 13 Снежинка (2 балла)

snowflake = int(input('Введите нечетное число: '))
a = [["."] * snowflake for i in range(snowflake)]
for i in range(snowflake):
    a[i][i] = "*"
    a[i][snowflake // 2] = "*"
    a[snowflake // 2][i] = "*"
    a[i][(snowflake - 1)- i] = "*"
for row in a:
    print(' '.join([str(elem) for elem in row]))

# Задача 14 Транспонирование матрицы (3 балла)

m=[[1, 1, 1],
[2, 2, 2],
[3, 3, 3],
[4, 4, 4]]
matrix_t = list(zip(*m))

print(m)
print(matrix_t)

# Задача 16 Составление базы данных (3 балла)
F = {'Ксюша': 22, 'Иван': 24, 'Антон': 25, 'Маша': 26, 'Дима': 24, 'Катя': 22}
del(F['Ксюша'])
print(F)
sum_v = 0
for key, value in F.items():
    sum_v += value
print(sum_v/len(F))

# Задача 15 (1 балл)
# Пользователь задает число $n$. Необходимо вернуть словарь, где ключами бы являлись числа от -(n-1) до (n-1), а значения - квадраты этих чисел.
n = int(input('Введите числО:'))
J = dict([(n, n**2)])
print(J)


# Задача 18 Перевод с эльфийского (5 баллов)
text_sindarin = ['Ilu,', 'varta', 'inye,', 'ruc-', 'sina', 'ana,', 'nen', 'ruc-', 'ana,', 'Arda', 'ana,', 'vista,',
    'limbe', 'et', 'ma', 'na-', 'auta-', 'a,', 'ava', 'er-', 'man', 'nan', 'os', 'sina', 'ilquen', 'horya', 'et',
    'alta', 'corma', 'nelde', 'na-', 'elda', 'ilfirin', 'onna', 'ngola,', 'a,', 'faila', 'et', 'ilquen', 'mar-,',
    'otso', 'dancil', 'norno,', 'alta', 'farea', 'a,', 'curuvar', 'oron', 'felya,', 'nerte', 'nerte', 'corma', 'na-',
    'firya', 'qwanur', 'ya', 'ilqua', 'here', 'ana,', 'sina', 'corma', 'na-', 'tuo', 'here', 'or', 'ilya', 'et',
    'lie', 'ananta', 'ilquen', 'toi,', 'gweria', 'nan', 'ma', 'na-', 'yando', 'er,', 'corma', 'ana,', 'nore',
    'mordor', 'ana,', 'sa,', 'oron', 'morna', 'harya-', 'sauron', 'lomba', 'er', 'corma', 'ilquen', 'nan', 'a,',
    'ana,', 'sina', 'corma', 'se', 'ilquen', 'alica', 'ilquen', 'umea', 'a,', 'ilquen', 'here', 'or', 'ilquen',
    'mar-,', 'er,', 'corma', 'tur-', 'ilquen']

dictionary_from_sindarin = {'Arda': 'земля', 'Ilu,': 'мир', 'a,': 'и', 'alica': 'жестокость', 'alta': 'великое',
    'ana,': 'в', 'ananta': 'но', 'auta-': 'уйти', 'ava': 'не', 'corma': 'кольцо', 'curuvar': 'мастеровой',
    'dancil': 'повелитель', 'elda': 'эльф', 'er': 'единый', 'er,': 'один', 'er-': 'остаться', 'et': 'с',
    'faila': 'справедливый', 'farea': 'добытчик', 'felya,': 'пещера', 'firya': 'человеческий', 'gweria': 'обмануть',
    'harya-': 'властелин', 'here': 'власть', 'horya': 'начаться', 'ilfirin': 'бессмертный', 'ilqua': 'всего',
    'ilquen': 'весь', 'ilya': 'каждый', 'inye,': 'я', 'lie': 'народ', 'limbe': 'многий', 'lomba': 'тайно',
    'ma': 'что', 'man': 'кто', 'mar-,': 'жить', 'mordor': 'мордора', 'morna': 'тёмный', 'na-': 'быть',
    'nan': 'другой', 'nelde': 'три', 'nen': 'вода', 'nerte': 'девять', 'ngola,': 'мудрый', 'nore': 'страна',
    'norno,': 'гном', 'onna': 'создание', 'or': 'над', 'oron': 'гора', 'os': 'о', 'otso': 'семь', 'qwanur': 'род',
    'ruc-': 'чувствовать', 'sa,': 'огонь', 'sauron': 'саурон', 'se': 'он', 'sina': 'этот', 'toi,': 'они',
    'tuo': 'сила', 'tur-': 'править', 'umea': 'злоба', 'varta': 'измениться', 'vista,': 'воздух', 'ya': 'который',
    'yando': 'ещё'}

text = ''
pos_dict = {}

# собираем словарь позиций слов из развернутого массива
# чтобы получить первые позиции слов в качестве ключей
for index in (range(len(text_sindarin) - 1, -1, -1)):
    selected_word = dictionary_from_sindarin[text_sindarin[index]]
    pos_dict[selected_word] = index
print(index, selected_word)

# собираем реальный текст
for index, word in enumerate(text_sindarin):
    text += dictionary_from_sindarin[word] + ' '
print(dictionary_from_sindarin[word])

# заполняем исходный массив пустыми значениями
for index, element in enumerate(text_sindarin):
    text_sindarin[index] = '<потеряно>'

# используя словарь позиций слов пытаемся восстановить текст в исходном массиве
for key, value in pos_dict.items():
    text_sindarin[value] = key

# собираем получившийся из словаря позиций текст
text = ''
for element in text_sindarin:
    text += element + ' '
print(text)

# считаем разницу
print(len(text_sindarin) - len(pos_dict.keys()))