# for k, v in {1:'1', '1':1}.items():
#     print(k, v)

# nums = [0,1,2,3,4,5]
# nums.append(nums[:])
# print(len(nums))

# data = {tuple():1}
# print(data)

# SPIRAL

# n = int(input()) # (0, 0) (0, 1) (0, 2)
# d = {}              # (1, 0) (1, 1) (1, 2)
# for i in range(n):
#     for j in range(n):
#         d[i,j] = 0
# x, y = 0, 0
# dx, dy = 0, 1
# d[x, y] = 1
# for k in range(2, n*n + 1):
#     while True:
#         x_n, y_n = x + dx, y + dy
#         if d.get((x_n, y_n), -1) == 0:
#             d[x_n, y_n] = k
#             x += dx
#             y += dy
#             break
#         else:
#             if (dx, dy) == (0, 1): dx, dy = 1, 0 # право ->
#             elif (dx, dy) == (1, 0): dx, dy = 0, -1 # вниз ->
#             elif (dx, dy) == (0, -1): dx, dy = -1, 0  # влево ->
#             elif (dx, dy) == (-1, 0): dx, dy = 0, 1  # вверх ->
#
# for i in range(n):
#     for j in range(n):
#         print(d[i,j], end = ' ')
#     print()


# d = {}
# d[(1,2)] = [3,4]
# print(d.get((1,2), 123))
# d.get(0, 123)
# print(d)


# dct = {1:111, 2:222, 3:333}
# print(dct.setdefault(3, -1))
# print(dct)

# abc = {1:'111', 2:'222'}
# print(abc.get(3, '333'))
# print(abc)

# n=int(input())
# d = {}
# for i in range(n):
#     s = input().split()
#     d.setdefault(s[0], s[1])
#     d.setdefault(s[1], s[0])
# print(d)
# while True:
#     q = input('Введите слово -->')
#     if q == 'stop':
#         break
#     print(d.get(q, 'Нет в словаре'))

# d = {1:111, 2:222, 3:333}
# for k, v in d.items():
#     print(k, v)

# s = list(map(int, input().split()))
# print(s)
# d = {}
# for i, j in enumerate(s):
#     print(i, j)
#     d[j] = d.get(j, [])
#     d[j].append(i)
# print(d)


# d = {1:11, 2:22}
# print(list(d.values()))

# a = {1:11,2:22}
# d = dict.fromkeys(a)
# print(d)

# a = {1:11, 2:22}
# b = {4:44, 5:55}
# a.update(b)
# print(a)

# a={1:11, 2:22, 3:33}
# print(sorted(a))


#
# d={}
# while True:
#     s = input('Введите товар и количество -->')
#     if s == '0':
#         break
#     print(s)
#     z = s.split()
#     d[z[0]] = d.get(z[0], 0) + int(z[1])
# for i in sorted(d, reverse = True):
#     print(i, d[i])


# print(divmod(13,4))

# f = float(input())
# print(type(f))

# a = float('inf')
# print(a**2)

# print(int('16', 8))

# sec = int(input())
# s = sec % 60 - остаток от деления


# print(200000000000000000000000000.0)
# 2e+26

# x = 99_9_99
# #Игнор подчерков в числах
# print(x)

# print(-2**308)

# import math
# print(math.pi)

# n = 4 + 3j
# print(n*2)

# n = int(input('Введите число > 0 -->'))
# for i in range(2, n):
#     if n % i == 0: #делится нацело
#         print('Составное')
#         break
# else: print('Простое')


# x = True
# y = False
# print(x)
# print(int(x))

# Вывести коды больших латинских букв:
# s = ord('A')
# n = ord('Z')
# for i in range(s,n):
#     print(i, chr(i))

# a = 324
# b = 324
# print(a is b)

# Year = int(input())
# if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
#     print('Високосный')
# else: print('Нет')

# a is None

t = input()
g = []
s = []
for i in t:
    if i in 'aeiou':
        g.append(i)
    else:
        s.append(i)
print(s)
print(g)
if len(g) - len(s) > 1:
    print('Impossible')
if len(g) > len(s): s, g = g, s
res = ''
for i in range(len(g)):
    res += s[i]
    res += g[i]
print(res)
if len(s) > len(g):
    res += s[-1]
print(res)
