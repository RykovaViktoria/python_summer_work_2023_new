# n = int(input())
# for k,v in d.items():
#     while n>=k:
#         res += v
#         n -=k
# print(res)

# import datetime, locale
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# a = datetime.datetime.today() + datetime.timedelta(days = 14)
# print(a)
# c = datetime.timedelta(days=1)
# for _ in range(10):
#     a+= c
#     print(a.strftime('%A %d, %B %Y'))

# import calendar
# year, month = map(int, input().split())
# print(calendar.monthcalendar(year, month))
# 2023 5
# [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 0, 0, 0, 0]]

# a = [1,2,3]
# b = 'abcde'
# from itertools import zip_longest
# for k in zip_longest(a,b, fillvalue = 0):
#     print(k)

# Тернарный оператор
# x, y = 5, 10
# ma = x if x > y else y
# print(ma)

# x = 'flip'
# def flip_flop(x):
#     return 'flop' if x == 'flip' else 'flip'
# for _ in range(5):
#     print(x := flip_flop(x))

# list comprehension
# Списковое включение

# print([ x**2 for x in range(20) if x % 3])
# формировать списки можно:
# 1) list
# 2) map
# 3) list comprehension

#1)  s = []
# for i in range(10):
#     s.append(i**3)
# print(s)

# 2) print(list(map(lambda x: x**3 , range(10))))
#
# 3) print([x**3 for x in range(10)])

# Построить списко четных чисел до 20ти вкл-но
# print([x for x in range(21) if x % 2 ==0])
#
# Условие в начале включения.
# original_prices = [1.25,-9.45,10.22,3.78,-5.92,1.16]
# prices = [i if i > 0 else 0 for i in original_prices]
# print(prices)


# prices = []
# original_prices = [1.25,-9.45,10.22,3.78,-5.92,1.16]
# for i, j in enumerate(original_prices):
#     if j < 0:
#         prices.append(0)
#     else:
#         prices.append(j)
# print(prices)

# from string import ascii_letters
# letters = 'hasвыпыр'
# print(ascii_letters)
# s = input()
# res = [f'{let} - EN' if let in ascii_letters else f'{let} - РУ' for let in s]
# print(res)

# from string import ascii_letters
# letters = 'hasвыпыр'
# print(ascii_letters)
# s = input()
# res = [f'{let} - EN' for let in s if let not in ascii_letters and let.isupper()]
# print(res)

# original_prices = [1.25,-9.45,10.22,3.78,-5.92,1.16]
# def get_price(price):
#     return price if price > 0 else 0
# new_price = [get_price(i) for i in original_prices]
# print(new_price)

# original_prices = [1.25,-9.45,10.22,3.78,-5.92,1.16]
# new_price = [(lambda x: 0 if x < 0 else x)(i) for i in original_prices]
# print(new_price)

# original_prices = [1.25,-9.45,10.22,3.78,-5.92,1.16]
# pos = [i for i in original_prices if i > 0]
# neg = [i for i in original_prices if i < 0]
# print(sum(pos) + sum(neg) == sum(original_prices))

# def fu(x):
#     return 'FizzBuzz' if x%15==0 else 'Fizz' if x%3 ==0 else 'Buzz' if x%5==0 else x
# a = [fu(i) for i in range(1,20)]
# print(*a)

# words = ['Я','изучаю','Python']
# res = [le for word in words for le in word]
# print(res)

# words = ['Я','изучаю','Python']
# print(list(''.join(words)))

key = ['name', 'age', 'weight']
value = ['Lilu', 25, 100]
res = [{x, y} for x in key for y in value]
print(res)

# mat = [[i for i in range(3)] for j in range(4)]
# print(mat)

# mat = [[(lambda x,y: x**y)(i,j) for i in range(1,5)] for j in range(4)]
# print(mat)

# mat = [[[(lambda x,y,z: x+y*10+z*100)(i,j,k) for i in range(2)] for j in range(4)] for k in range(2)]
# print(mat)

# бутылка кляйна из листа мёбиуса

# mat = [[[0,1,2],[3,4,5],[6,7,8]],
#        [[10,11,12],[13,14,15],[16,17,18]],
#        [[20,21,22],[23,24,25],[26,27,28]],
#        [[30,31,32],[33,34,35],[36,37,38]]]
# print(mat)
# flat = [k for i in mat for j in i for k in j]
# print(*flat)

# t = [[x * y for x in range(1,6)]for y in range(1,6)]
# print(t)

# import sys
# a = [i for i in range(1000000)]
# print(type(a), len(a), sys.getsizeof(a))
# b = (x for x in range(1000000)) #- генераторное выражение в круглых скобках
# print(type(b), sys.getsizeof(b))
# for i in b:
#     print(i)
#     input()
# Добавление в словарь:
# d = {}
# for num in range(1, 10):
#     d[num] = num * 2
# print(d)
# Генераторы словарей
# d = {}
# for num in range(1, 10):
#     d[num] = num ** 2
# print(d)
# t = {num: num**2 for num in range(1,10) if num %2 ==0}
# print(t)

# dict1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
# filt = {k:v for k,v in dict1.items() if v > 2}
# print(filt)

# dict1 = {'aaa':15, 'bbb':25, 'ccc':37, 'ddd':45, 'eee':5}
# filt = {k:v for k,v in dict1.items() if v > 25}
# print(filt)


# dict1 = {'aaa':15, 'bbb':45, 'ccc':37, 'ddd':45, 'eee':5}
# print(max(dict1.values()))
# fio = [k for k, v in dict1.items() if v == max(dict1.values())]
# print(fio)

#
# dict1 = {'aaa':15, 'bbb':45, 'ccc':37, 'ddd':45, 'eee':5}
# print(max(dict1.values()))
# fio = [(k,v) for k, v in dict1.items() if v == max(dict1.values())]
# print(fio)

# dict1 = {'aaa':15, 'bbb':45, 'ccc':37, 'ddd':45, 'eee':5}
# print(max(dict1.values()))
# fio = [(k,v) for k, v in dict1.items() if v == 45 and k.startswith('b')]
# print(fio)

# names = ['aaa', 'bbb', 'ccc', 'ddd']
# index = {k:v for (k,v) in enumerate(names, 1)}
# print(index)

# lst = ['ноль', 'один', 'два', 'три']
# dct = {str(k):v for k,v in enumerate(lst)}
# print(dct)
# n = int(input())
# st = [dct[i] for i in str(n)]
# print(*st)