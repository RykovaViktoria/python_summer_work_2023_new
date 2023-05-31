# import itertools
# for i in itertools.combinations([1,2,3,4,5],3):
#     print(i)
#
# Обработка исключений
#
# a = [2100,200]
# while True:
#     i = int(input('введите правильный индекс -->'))
#     try:
#         print(a[i])
#     except:
#         print('Нет индекса')
#     else:
#         print('ok')

# try:
#     1/0
# except ZeroDivisionError as e:
#     print(e)
# else IndexError:
#     print('else')
# finally:
#     print('Finally')

# while True:
#     try:
#         n = int(input('Введите число -->'))
#         print(n)
#     except ValueError:
#         print('Ошибка ввода')
#     except Exception:
#         print('Другая ошибка')
#     else:
#         print(n)
#         break

# while True:
#     s = input()
#     try:
#         f = open(s)
#     except FileNotFoundError:
#         print('Не найден')
#     else:
#         print(f'Файл {s} найден!')

# == - проверка на рав-во
#

# tf = True
# while tf:
#     s = input()
#     try:
#         f = open(s)
#     except FileNotFoundError:
#         print('Не найден')
#     else:
#         print(f'Файл {s} найден!')
#         tf = False

# lst = [1078, 1091, 1083, 1080, 1082, 32, 1085, 1077, 32, 1074, 1086, 1088, 1091, 1081, 32]
# for i in lst:
#     print(chr(i))
#yield - генератор
# def fun(n):
#     print(111, n)
#     for x in range(n):
#         print(222, x)
#         yield x*x - застывание
#         print(333, x)
# g = fun(3)
# print(555, g)
# for i in g:
#     print(444, i)

# def fun(n):
#     for x in range(n):
#         print('До yield', x)
#         yield 2*x #- передается в k
#         print('После 1')
# g = fun(5)
# for k in g:
#     print('Перед печатью')
#     print(f'{k=}')
#     print('После 2')
#     input() #- для отладки

# def fun(n):
#     for x in range(n):
#         yield 2**x
#
# g = fun(5)
# for k in g:
#     print(f'{k=}')

# def fun(n):
#     for x in range(n):
#         if x % 2 ==0:
#             yield x**2
#         else:
#             yield x**3
# g = fun(10)
# for k in g:
#     print(k)

# def fun(n):
#     for x in range(n):
#         yield x ** 3 if x % 2 else x ** 2
# g = fun(10)
# for k in g:
#     print(k)

# def fun(n):
#     for x in range(n):
#         yield x ** 3 if x % 2 else x ** 2
# g = fun(3)
# for _ in range(10):
#     try:
#         print(next(g))
#     except StopIteration:
#         print('Stop')
#         break
# print('StopStop')

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def fact():
#     f,k = 1,1
#     while True:
#         print(k, f)
#         yield f
#         k += 1
#         f *= k
# gf = fact()
# for m in gf:
#     print(f'{m=}')
#     input()

# def fact():
#     f,k = 1,1
#     while True:
#         print(k, f)
#         yield f
#         k += 1
#         f *= k
# gf = fact()
# while True:
#     print(next(gf))
#     input() # - как останов

# def fact():
#     f,k = 1,1
#     while True:
#         print(k, f)
#         yield f
#         k += 1
#         f *= k
# gf = fact()
# for _ in range(int(input())):
#     print(next(gf))

# def fact():
#     f,k = 1,1
#     while True:
#         print(k, f)
#         yield f
#         k += 1
#         f += k
# gf = fact()
# for _ in range(int(input())):
#     print(next(gf))

# def sum_list(lst):
#     i = 1
#     while True:
#         i +=1
#         yield sum(lst[:i])
#
# lst = list(map(int,input().split()))
# gen_sum = sum_list(lst)
# for _ in range(len(lst)):
#     print(next(gen_sum))

#Проверить работу на 1 значении и на пустом списке.


# def sum_list(lst):
#     cur_sum = 0
#     i = 0
#     while True:
#         cur_sum += lst[i]
#         yield cur_sum
#         i += 1
#
# lst = list(map(int,input().split()))
# gen_sum = sum_list(lst)
# for _ in range(len(lst)):
#     print(next(gen_sum))


# def sum_list(lst):
#     cur_sum = 0
#     i = 0
#     while True:
#         if i >= len(lst):
#             return
#         cur_sum += lst[i]
#         yield cur_sum
#         i += 1
#
# lst = list(map(int,input().split()))
# gen_sum = sum_list(lst)
# for _ in range(len(lst)):
#     print(next(gen_sum))

def gen():
    i = 0
    while True:
        i += 1
        for j in range(i):
            yield i


gener = gen()
for i in range(int(input())):
    print(next(gener), end = ',')

