# СЛОВАРИ# print(2**3**2)


# tes = set()

# tes = {2.0, 'abc', (1,2,3), 1,2,3}
# print(tes)

# tes = {}
# -словарь, а не множество!

# lst = [1,2,2,3,3,3,4,4,4,4]
# print(len(lst))
# lst = set(lst)
# print(len(lst))

# m = {'jan', 'feb', 'mar', 'apr', 'may', 'jun'}
# for i in m:
#     print(i)
# print('mar'in m)
# по индексу нельзя обратиться, срезы тоже нельзя

# Проверить время работы программы:
# from time import time
# t0 = time()
# for i in range(1000000):
#     pass
# print(time() - t0)

# from time import time
# number = 15000
# my_set = set(range(number))
# my_list = list(range(number))
# my_tuple = tuple(range(number))
# my_dict = {}
# t1 = time()
# for i in range(number):
#     if i in my_set:
#         pass
# print(f'Операция с множеством: {time() - t1} секунд')
# t2 = time()
# for i in range(number):
#     if i in my_list:
#         pass
# print(f'Операция со списком: {time() - t2} секунд')
# t3 = time()
# for i in range(number):
#     if i in my_tuple:
#         pass
# print(f'Операция с кортежем: {time() - t3} секунд')
# t4 = time()
# for i in range(number):
#     if i in my_dict:
#         pass
# print(f'Операция со словарем: {time() - t4} секунд')
#
# Операция с множеством: 0.0011289119720458984 секунд
# Операция со списком: 1.558967113494873 секунд
# Операция с кортежем: 1.0905258655548096 секунд
# Операция со словарем: 0.0010309219360351562 секунд

# for i in range(10):
#     print(f'{i=}')
# i=0
# i=1
# i=2
# i=3
# i=4
# i=5
# i=6
# i=7
# i=8
# i=9

# for i in range(11):
#     print(f'{i:3}') - хотим, чтобы число заняло 3 позиции (выравнивает столбец)

# for i in range(5,11):
#     print(f'{i:05}')
# 00005
# 00006
# 00007
# 00008
# 00009
# 00010

# a = 123.456789
# print(f'{a=:10.2f}') #- 2 знака после запятой, и чтобы 10 позиций заняло
# a=    123.46

# i = 2
# if q:= i*i >3:
#     print(q)
#
# pass - пропустить
#
# n = int(input())
# match n:
#     case 0: print('0')
#     case 1: print('1')
#     case other: print('other')

# tes = set(map(int, input().split()))
# print(f'tes={tes}')
# print(sum(tes)/len(tes))

# import sys
# print(sys.version)

# tes = {1,22,3}
# tes.discard(1)
# tes.add(0)
# tes.remove(22)
# print(tes)


# tes1 = {11,22,33,44,55}
# tes2={11,22,'abc','cde'}
# print(tes2.union(tes1))


# s = input()
# s = set()
# alph = set("абвгдеёжзийлмнопрстуфхцчшщъыьэюя")
# print(s==alph)

# print(set("123") | set ('456'))
# print(set('123')&{123})

# x = {1,2,3}
# y = {4,3,6}
# z = x.intersection(y)
# print(z)

# x = {1,2,3}
# y = {4,3,6}
# print(x^y)

# s = input().split()
# print(s)
# d = set()
# for i in s:
#     d = d | set(i)
#     print(f'{i=} {set(i)=}{d=}')
# print(len(d))

# def summ(x,y):
#     result = x + y
#     return result
# def sub(x,y):
#     return x - y
# print(sub(3,4))

# def convert_to_celsius(temp):
#     result = (5/9)*(temp - 32)
#     return result
# x = convert_to_celsius(40)
# print(x)

# def convert_to_f(temp):
#     result = 9/5 * temp +32
#     return result
# s = int(input())
# print(convert_to_f(s))

# Расчет подоходного налога:
# y = int(input())
# x = 13
# def tax(money):
#     result = x/100*money
#     return result
# print(tax(y))


# def tax(money, pn=13):
#     result = pn/100*money
#     return result
# y = int(input())
# print(tax(y, 15))

# def empty(var1,var2):
#     pass

