# s = '12345'
# for i in s:
#     print(s)
#     s = ''
#
# def translate(t):
#     n = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XC':90,'XL':40,'CD':400,'CM':900}
#     s = input()
#     while True:
#         if not s: break
#         for k,v in d.items():
#             if s.startswith(k):
#                 res += v
#                 s = s[len(k):]
#                 break
#         print(f'{res=} {s=}')
#     print(res)


# def f(*args):
#     for i in args:
#         s *= i
#     return s
#
# print(f(1,3,4))

#
# def f(**kwargs):
#     print(type(kwargs))
#     res =1
#     for k, v in kwargs.items():
#         res *= v
#     return f"{res=}"
# print(f(name=30, age=20))

# def f(**kwargs):
#     res = 1
#     string = ''
#     for k, v in kwargs.items():
#         if type(v) == int:
#             res *= v
#         elif type(v) == str:
#             string += v
#     return res, string
# print(f(name=30, age = 20, Name='Nick', surname = 'Smirnov'))

# def many_all(var1, var2,*args, **kwargs):
#     print(var1)
#     print(var2)
#     print(kwargs)
# many_all(10,34,77,name = 'Piter', age =20)
#
# def pod_nalog(income, share = 13):
#     return income*share/100
# print(pod_nalog(100))
# print(pod_nalog(100, share = 13))
# print(pod_nalog(100, share = 15))

# def uni_let(lst):
#     tes = set()
#     for i in lst:
#         for j in i:
#             tes.add(j)
#         return tes, len(tes)
#     sorted_tes = sorted(tes)
#     res1 = ''.join(sorted_tes)
#     return res1, len(res1)
#     print(res1)
#
# print(uni_let([]))
# print(uni_let(['definition']))
# print(uni_let(['definition', 'solution']))

# def f(n):
#     def f1(p):
#         return p * p
#     def f2(w):
#         return w + w
#     if n < 10:
#         return f1(n)
#     else:
#         return f2(n)
#
# x = int(input())
# print(f(x))

# def check2(n):
#     def chet(i):
#         print(i, "Четное")
#         return i * i
#     def nechet(i):
#         print(i, "Нечетное")
#         return i ** 3
#     if i % 2 != 0:
#         res = nechet(i)
#     else:
#         res = chet(i)
#     return res
# n = int(input())
# for i in range(n+1):
#     print(check2(i))

# x = 10
# def doubling(y):
#     z = y*y
#     print(y, z)
# doubling(x)
# print(z) - z в локальной области видимости, поэтому мы не можем вызвать print(z) извне

# s = 0
# print('000', s)
# def a():
#     global s
#     s=1
#     print('111', s)
#     def b():
#         #global s
#         s= 2
#         print('222', s)
#     b()
#     print('333', s)
# a()
# print('444', s)
# s=3
# print('555', s)

# def counter():
#     num = 0
#     def incr():
#         nonlocal num
#         num += 1
#         return num
#     x = incr()
#     return x
# inc = counter()
# print(inc)

# def fb(i):
#     def fb3():
#         return 'FIZZ'
#     def fb5():
#         return 'BUZZ'
#     def fb15():
#         return 'FIZZBUZZ'
#     def fb_other(i):
#         return str(i)
#
#     if i % 15 == 0: res = fb15()
#     elif i % 3 == 0: res = fb3()
#     elif i % 5 == 0: res = fb5()
#     else: res = fb_other(i)
#     return res
# for i in range(int(input())+1):
#     print(fb(i))

# i = 3
# print(bool(i % 2))

# help(bool)

# zip([1,2,3,4], 'abc')

# help(zip)

# a = zip([1,2,3,4], 'abcd', ('A', 'Б')) for k in zip([1,2,3,4,5], 'abcdef'):
# a = zip(((1,2,3,4), {1:111, 2:222}, {123,456,789}))
# for i in a:
#     print(i)

# print(list(filter(bool, [0, 1,2,3,4])))

# def chet(x):
#     return 1 - x % 2
# print(list(filter(chet, [0, 1,2,3,4])))

# x = 1
# for i in range(10):
#     x = - x
#     print(x)

# print(any((True, False)))

# print(all([[[]]]))

# print(list(map(int, input().split())))

# k = 123
# s = str(k)
# d = list(map(str, s))
# print(d)

# def sba(x):
#     return - abs(x)
# print(sorted([1,4,5,-4,6], key = sba, reverse = True))

# def fu(lst, x):
#     res = []
#     for i in lst:
#         if i*i > x:
#             res.append(i*i)
#     return res
# print(fu([1,10,100], -500))

# def fu(lst, x):
#     def fltr(i):
#         return i*i > x
#     return list(filter(fltr, lst))
# print(fu([1,10,100], -500))

# help(filter)