# print(bool(0,))
# import math
# print(math.sqrt(9))

# import math
# print(math.sqrt(9), math.pi)

# import math
# print(pi, sqrt(9))

# import math
# print(math.lcm(12, 17))

# import math
# def circle(r):
#     return math.pi*r*r
# print(circle(float(input(''))))


# import math
# def circle(d):
#     return math.pi*d*0.25
# print(circle(float(input(''))))

# import pandas as pd
# pd.DataFrame

# help('modules')

# t = [(1,2), (0,2), (1,1), (0,0),(0,1),(1,0)]
# def fu(p):
#     return -p[0], p[1]
# print(sorted(t, key = fu))

# lst = [123, 201, 34, 2, 555, 42]
# def last_digit(x):
#     return x % 10
# print(sorted(lst, key = last_digit))
# [201, 2, 42, 123, 34, 555]
# стабильная сортировка (2 перед 42 как в изначальном списке)

# сортируем по возрастанию или убыванию самих чисел (два параметра у return) return x % 10, -x
# lst = [123, 3, 201, 34, 222, 555, 42]
# def last_digit1(x):
#     return x % 10, -x
# print(sorted(lst, key = last_digit1))

# exec('x=5')
# print(exec('print(x)'))

# print('широка страна моя родная'.partition('моя'))
# ('широка страна ', 'моя', ' родная')

# s = 'АГЦТТФГЦЦ'
# def repeat(s, n):
#     d = {}
#     for i in range(len(s)-n+1):
#         d[s[i:i+n]]=d.get(s[i:i+n], 0) + 1
#     ma = max(d.values())
#     res = []
#     for k, v in d.items:
#         if v == ma:
#             res.append(k)
#     return res
# print(repeat(s,3))

# s = "АГЦТАААГГГГГГГГГГГГЦЦТ"
# def c(s, n):
#     d = {}
#     for i in range(len(s) - n + 1):
#         if s[i] not in d:
#             d[s[i:i + n]] = 1
#         d[s[i: i + n]] += 1
#     ma = max(d.values())
#     return ma, d
# print(c(s, 2))

# spi = [222,21,1,111,12,322]
# print(sorted(spi, key = lambda x: x % 10))

# spi = [222,21,1,111,12,322]
# print(sorted(spi, key = lambda x: (x % 10, x)))

# spi = [222,21,1,111,12,322]
# print(sorted(spi, key =

# print((lambda x: x+1)(2))

# for i in range(10):
#     print((lambda x:x*x)(i))

# for x in range(10):
#     print((lambda x:x*x)(x))
#
# add_one = lambda x: x + 1
# print(add_one(10))

# add_one = lambda x, n: x**n
# print(add_one(10, 11))

# add_one = lambda x, n: x**n
# print(add_one(10, 11))

# add_one = lambda *args: len(args)
# print(add_one(10, 11))

# add_one = lambda lst: sum(lst)
# print(add_one([10, 11, 45 ,67]))

# full_name = lambda first, last: f"Full name: {first} {last}"
# print(full_name('Mike', 'Tyson'))

# x = 'ascf'
# str = lambda x: x.lower()[::-1]
# print(str(x))

# x = 'ascf'
# str = lambda x: len(x.lower()[::-1])
# print(str(x))

# l = lambda s = 'ABCD': s.lower()[::-1]
# print(l())

# l = lambda x, n: x **n
# print(l(3,4))


# lst = [11, 22, 12, 21, 33, 555, 6]
# print(sorted(lst, key = lambda x: (x % 2, x%10, -x)))  # -x по убыванию

# s = ['a', 'A', 'bB', 'aaa', 'C', 'ddd']
# print(sorted(s, key = lambda x: x.lower()))

# s = ['a', 'A', 'bB', 'aaaaa', 'C', 'ddd']
# print(sorted(s, key = lambda x: x[0].upper()))

# Найти самое близкое к числу 16 число в списке:
# lst = [1,2,3,4,5,6]
# x = 16
# print(min(lst, key = lambda y: abs(y - x)))

# t = (lambda x: x**2, lambda x:x**3)
# print(t[1](16))

# Dict = {
#     1: (lambda: print('Monday')),
#     2: (lambda: print('Tuesday'))
# }
# print(Dict[2]())

# numbers=[0,1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x: x % 3 == 0, numbers)))


# numbers=[0,1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x: x % 2, numbers)))

lst = [11,2,33,4,5,6]
print(list(map(lambda x: sum(map(int, str(x))), lst)))
