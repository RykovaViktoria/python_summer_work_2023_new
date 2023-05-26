# f = open("text.txt", 'r', encoding = 'utf-8')
# s = f.readlines()
# d=''
# for i in s:
#     d += str(i).lower()
# print(d)
# f.close()
#
# import collections
# a = collections.Counter(d)
# b = dict(a)
# f = (sorted(b.items(), key = lambda x: (-x[1], x[0]))[:10])
# print(f)
# for k,v in f:
#     print(f'{k} - {v}')

# from collections import Counter
# x = '''abs
# asfas
# asfa'''
# b = Counter(x)
# s = sorted(b.items(), key = lambda x: (-x[1], x[0]))
# for i,j in s[:10]:
#     print(f'{repr(i)} - {j}')
#
# s = input()
# print(s)
# for i in s:
#     print(i)
# Не надо делать list прямо в input() !

# d = {1:111,2:222,3:333}
# i = int(input())
# print(d[i])

d = {1:111,2:222,3:333}
i = int(input())
print(d.get(i, 'Нет в словаре'))