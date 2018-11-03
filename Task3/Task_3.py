# Задача 1 Сортировка (1 балл)
a = sorted(input("Введите числа: ").split(" "))
for i in a:
    print('%.3f' % float(i))

# Задача 2 Средний символ (1 балл)
st = str(input("Введите слово: "))
if len(st) % 2:
    q = len(st)/2
    qq = st[int(q)]
    print(qq)
else:
    p = len(st)/2
    pp = st[int(p)]
    print(st[int(p)-1] + st[int(p)])


# Задача 3 Еще одна задача со строками (1 балл)
f = (input("Введите предложение: ")).split(" ")
for i in f:
    print(i[::-1] if len(i) > 5 else i)


# Задача 4 ДНК (1 балл)
DNK = list(input("введите ДНК: "))
slovar = dict(A= "T", T = "A", G = "C", C = "G")
for i, value in enumerate(DNK):
    if value in slovar:
        DNK[i] = slovar[value]
print(str(DNK))


# Задача 5 Танцевальная музыка (1 балл)
music = 'BOOMWEBOOMAREBOOMBOOMTHEBOOMCHAMPIONSBOOMMYBOOMFRIENDBOOM'
print(music.replace('BOOM',' '))


# Задача 8 Смайлики (1 балла)
smail = [":-D",":)",";-D",":~D"]
text = input("Введите текст со смайлами: ").split(" ")
k = 0

for i in text:
    if i in smail:
        k+=1
print(k)

# Задача 9 "+1" (5 баллов)
text = "python33"

num = int(''.join(i for i in text if i.isdigit()) or '0') + 1
print("python" + str(num))

# Задача 10 "Волна" (1 балл)
text = 'Python'
index = 0
for index, value in enumerate(text):
    print(text[0:index] + value.upper() + text[index + 1:len(text)])
    index += 1