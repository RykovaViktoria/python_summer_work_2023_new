# d = 4
# e = 'hi'
# d, e = e, int(d)
# print(d, e)

# lang = 'Python'
# print(f"{lang + 'abc'} is the best!")

# print('All your     need    is    love'.split()) - удалит все пробелы
# print('All your     need    is    love'.split(' ')) - съест по 1 пробелу в пропусках

# print(chr(ord('a')))

# print('www.example.com'.strip('cmowz.'))

# print('Hello world'.startswith('Hell'))

# dict = {k:v}
# person={'name':'Маша', 'age': 25}
# person['name'] = 'Миша'
# s = 'name'
# print(person[s])

# dct = {1:11, 2:22, 1:111111}
# print(dct)
# for k in dct:
#     print(k, dct[k])

# dct = {1:11, 2:22, 3:333}
# lst = [0, 11, 22, 333]
# print(dct[1])
# print(lst[1])
# print(1 in dct)
# if 0 in dct:
#     print(dct[0])
# else:
#     print('No')
#     dct[0]=0
# print(dct)


# s = input()
# dct = {}
# for i in s:
#     if i not in dct:
#         dct[i] = 0
#     dct[i] += 1
# print(sorted(dct[i]))

# n = input()
# dct = {}
# for k in n:
#     if k not in dct:
#         dct[k]=0
#     dct[k] += 1
# print(dct)

# d = {True: 1, False: 0}
# c = {False: 0, True: 1}
# print(d ==c)

# d = {False:0, 1:123, True:1}
# print(d)
#
# Res = {False: 0, 1: 1}

# s = input()
# d = {'0': 'ноль', '1':'один', '2':'два', '3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь', '9':'девять'}
# for i in s:
#     print(d[i], end =' ')

# a = {}
# print(type(a))
# a[1] = 111
# print(a)
#
# c = dict(name = 'vvv', age = 16)
# print(c)

# d = dict(zip([1,2,3], [11,22,33]))
# print(d)

# m = {}
# for i in [1,3,5,7,8,10,12]:
#     m[i] = 31
# for i in [4,6,9,11]:
#     m[i] = 30
# m[2] = 28
# while True:
#     year = int(input('Year --'))
#     month = int(input('Month --'))
#     if year ==0 and month ==0: break
#     if year % 4 == 0 and month == 2:
#         print(29)
#     print(year, month)
#     print(m[month])

# d = {1:111, 2:222}
# del d[1]
# print(d)

# s = input().split()
# d = {}
# for i in s:
#     if i not in d:
#         d[i]=0
#     d[i] +=1
# print(d)
# ma, ms = 0, ''
# for k in d:
#     print(k, d[k], ma, ms)
#     if d[k] > ma:
#         ma = d[k]
#         ms = k
# print(ms, ma)

# d = {1:11, 2:22, 3:33}
# print(d.get(0, ''))

# s = input()
# dct = {}
# for k in s:
#     if k not in dct:
#         dct[k]=0
#     dct[k] +=1
# print(dct)

# s = input('Number:')
# dct = {}
# for k in s:
#     # print(k, dct)
#     dct[k]  = dct.get(k,0) + 1
#     # print(dct)
#     # input()
# print(dct)
#
# s = input().split()
# d = {}
# for k in s:
#     if k not in d:
#         d[k]=0
#     d[k] += 1
#     #print(k, '_', d[k], sep = '', end = ' ')
#     res += k+'_'+str(d[k])+' '
#
# print(res)

s = input('Ввеите 2 слова через пробел -->').split()
d = {}
for k in s:
    if k not in d = 0











