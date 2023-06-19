# lst = [1,2,3,4,5]
# for x in lst:
#     print(x)
#     a = lst.pop()
#     print(a, lst)
# print(lst)

# lst = [1,2,3,4,5]
# for x in lst:
#     print(x)
#     a = lst.pop(0)
#     print(a, lst)
# print(lst)

# def func(x):
#     return print(x*x)
# a = 5
# b = func(a)
# print(b)

# def div(x,y):
#     return x / y
# try:
#     result = div(100,0)
#     print('ok')
# except (ZeroDivisionError, KeyError) as e:
#     print(e)

# def div(x,y):
#     return x / y
# try:
#     result = div(100,1)
#     a = [1]
#     print(a[345])
#     print('ok')
# except (ZeroDivisionError, KeyError) as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except Exception as e:
#     print(e)

# def div(x,y):
#     try:
#         out = x / y
#     except:
#         try:
#             import math
#             out = math.inf * x / abs(x)
#         except:
#             out = None
#     finally:
#         return out
#
# print(div(15,3))
# print(div(15,0))
# print(div(-15,0))
# print(div(0,0))

# try:
#     raise Exception('какой-то текст')
# except Exception as e:
#     print(e)

# def validate(name):
#     if len(name) < 10:
#         raise ValueError
#
# try:
#     name = input()
#     validate(name)
# except ValueError:
#     print('короткое')

# class MyException(ValueError):
#     pass
# def validate(name):
#     if len(name) < 10:
#         raise MyException
# validate(input())

#Когда слова начинаются с большой буквы (ValueError) - стиль верблюда

# class Positive(ValueError):
#     pass
# class Negative(ValueError):
#     pass
# def fu(lst):
#     for i in lst:
#         try:
#             if i > 0: raise Positive('Положительное')
#             elif i < 0: raise Negative('Отрицательное')
#             else: print(0)
#         except Positive as e: print(e)
#         except Negative as e: print(e)
#     return('Finish')
# print(fu([-1,0,1,-4,5,-6]))


# def fun(n):
#     for x in range(n):
#         yield x * x
# g = fun(3)
# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break

# def fact():
#     f, k = 1, 1
#     while True:
#         yield f
#         k += 1
#         f *= k
#         if k > 10:
#             return
# gf = fact()
# print(type(gf), type(fact()), type(fact))
#
# while True:
#     try:
#         print(next(gf))
#     except StopIteration:
#         break

# def fact():
#     f, k = 1, 1
#     while True:
#         yield f
#         k += 1
#         f *= k
#         if k > 5:
#             break
#     return
# gf = fact()
# print(type(gf), type(fact()), type(fact))
# for m in range(20):
#     try:
#         print(next(gf))
#     except StopIteration:
#         break

# def rep123():
#     yield 1
#     yield 2
#     yield 3
# print(*rep123())
# print(2 in rep123())
# n1, n2, n3 = rep123()
# print(n1, n2, n3)

# def rep123():
#     yield 1
#     yield 2
#     yield 3
# gen = rep123()
# #print(*gen)
# print(2 in gen)
# print(next(gen))
# print(n1)
# print(n1, n2, n3)

# def rep123():
#     yield 1
#     yield 2
#     yield 3
# gen = rep123()
#
# print(next(gen))
# print(next(rep123())) - создает генератор заново как бы

# def fun_gen(n):
#     yield from [1,2,3]
# for i in fun_gen(5):
#     print(i)

# def fun_gen(n):
#     yield from [1,2,3]
# for i in fun_gen(5):
#     print(i)

# def f1():
#     yield 'r'
#     yield 'g'
#     yield 'b'
# def f2():
#     yield 111
#     yield from f1()
#     yield 222
# print(*f2())

# def f1():
#     yield 'r'
#     yield 'g'
#     yield 'b'
# def f2():
#     yield 111
#     yield from f1()
#     yield 222
#
# for i in f2():
#     print(i)

# def f1():
#     yield 'r'
#     yield 'g'
#     yield 'b'
# def f2():
#     yield from f1()
#     yield from f1()
#     yield from f1()
#
# for i in f2():
#     print(i)

# lc = [x for x in range(10)]
# print(lc, type(lc))
# gen_expr = (x for x in range(10))
# print(type(gen_expr))
# print(gen_expr)
# # print(*gen_expr)
# print(next(gen_expr))
# for i in gen_expr:
#     print(i)

# def integers(n):
#     yield from range(1, n+1)
# def evens(iterable):
#     for i in iterable:
#         if not i%2:
#             yield i
# def sq(iterable):
#     for k in iterable:
#         yield k*k
#
# chain = sq(evens(integers(10)))
# print(*chain)

# def n65():
#     for i in range(65, 91):
#         yield i
# def ch(iterable):
#     for i in iterable:
#         yield(chr(i))
# print(*ch(n65()))

# def n65():
#     for i in range(65, 91):
#         yield i
# def ch(iterable):
#     for i in iterable:
#         yield(chr(i))
# print(*ch(n65()))

# def n65():
#     a = ord('а')
#     for i in range(a, a + 32):
#         yield i
#         if i == ord('е'):
#             yield ord('ё')
# def ch(iterable):
#     for i in iterable:
#         yield(chr(i))
# print(*ch(n65()))

# print(ord('ё')) - 1105

# Рекурсия

# def func(n):
#     print('func', n)
#     input()
#     n -= 1
#     if n > 0:
#         func(n)
# func(5)
#
# def func(n):
#     print('func1', n)
#     input('-->')
#     n -= 1
#     if n > 0:
#         func(n)
#     print('func2', n)
#     input('==>')
# func(5)


# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(4))

def fact(n):
    if n == 1:
        return 1
    else:
        x= n*fact(n-1)
        print(x, n)
        return x
print(fact(4))

# def triangle(n):
#     if n == 0:
#         return ''
#     else:
#         print('*'*n)
#         triangle(n-1)
# triangle(5)
#
# *****
# ****
# ***
# **
# *


# def triangle(n):
#     if n == 0:
#         return ''
#     else:
#         triangle(n-1)
#         print('*'*n)
# triangle(5)
#
# *
# **
# ***
# ****
# *****

# print(sum(range(10)))


# def sumn(n):
#     if n==0:
#         return 0
#     else:
#         return n + sumn(n-1)
#
# print(sumn(5))

# def fibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# print(fibo(5))


