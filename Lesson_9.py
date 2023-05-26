# Вложенные словари:

# x = ['asdda','rtywew', 'dfagy']
# print(sorted(x, key = lambda y: (-len(set(y)), y)))

# spisok = [222,31,1,711,82,322]
# print(sorted(spisok, key = lambda x: str(x)[0]))

# Число из списка, у которого сумма цифр наименьшая:
#
# spisok = [222,31,711,82,322]
# print(min(spisok, key = lambda x: sum(map(int, list(str(x))))))

# s = list(input())
# print(s)

# x, y = 1,2
# ma = x if x > y else y

# d = int(input())
# print((lambda x: x * 0.13  if x <= 5000000 else 5000000*0.13+(x-5000000)*0.15)(d))

# lst =[('Петров', 100), ('Иванов', 200), ('Герасимов', 500)]
# print(sorted(lst, key = lambda x: (-x[1], x[0])))

# st = {0:{'name':'Иванов', 'age':22},
#             1:{'name':'Сидоров', 'age':23},
#             2:{'name':'Петров', 'age':24}}
#
# for k,v in st.items():
#     for i,j in v.items():
#         print(k, i, j)

# dct = {1:123, 2:'234', 3:{1:111,2:222}, 4:{1:'abc', 2:'def'}}
# x = 1
# for k, v in dct.items():
#     if k == x:
#         print(v)
#     if type(v) == dict:
#         for p, q  in v.items():
#             if p == x:
#                 print(q)


import collections
x = 'ырывряыпыаюпрвыюарпягарпфдукгряпваряв'
a = collections.Counter('С помощью Counter определите, какая буква содержится больше всего в строке x')
b = dict(a)
print(sorted(b.items(), key = lambda x: -x[1])[:3])

# Работа с файлами:

