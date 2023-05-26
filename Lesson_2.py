# n=123
# s='abc'
# print(f'{n:4}__{s}')

# s = 'abra cad abra'
# lst = s.split()
# x = '\n'.join(lst)
# print(x)

# s = 'kazak'
# n=len(s)
# for i in range(n // 2):
#     print(s[i])
#     if s[i] != s[n-i-1]:
#         print(False)
#         break
# else:
#     print(True)

# s = 'Широка страна моя родная'
# print(s.split(maxsplit = 2))

# lst = [10, True, [1,2], 'abcdef']
# # n = len(lst)
# # for i in range(n):
# #     print(i, lst[i])
# lst.append(123)
# print(lst)

# n = int(input())
# lst = []
# for i in range(1, n+1):
#     for _ in range(i):
#         lst.append(i)
# print(lst)
# print([n] * n)

# t = [1,-2,3,-4, 5,-6,7,-8]
# t.sort()
# # print(t)
#
# ab =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# res = []
# for i in range(26):
#     res.append(ab[i]*(i+1))
# print(res)

# i = 5
# while i <= 15:
#     print(i)
#     i += 2

# lst = []
# while True:
#     n = int(input())
#     if n < 0:
#         break
#     lst.append(n)
# print(sum(lst))

# x,y,z = 1,2,3
# print(x)

# list = chr(97:123)
# print(list)
#
# n = (123,234,345,456,567,678,789,890)
# s = (int(input()),)
# n += s
# l = list(n)
# l.sort()
# o=tuple(l)
# print(o)

t = (1,2,3, [11,12,13])
t[3].append(44)
print(t)