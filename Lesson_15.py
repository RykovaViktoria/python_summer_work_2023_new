# def f(x,y):
#     try:
#         return x/y
#     except:
#         return x, y
#     finally:
#         print('finally')
# print(f(1,2))
#
# finally
# 0.5

# d = {}
# res = {}
# def fibo(n):
#     d[n] = d.get(n,0) + 1 #- посчитаем, сколько раз вызывалась каждая n
#     if n not in res:
#         if n == 1: return 0
#         elif n == 2: return 1
#         else: res[n] = fibo(n-1) + fibo(n-2)
#     return res[n]
# print(fibo(15))
# print(d)

# def fibo(n):
#     match n:
#         case 1: return 0
#         case 2: return 1
#         case _: return fibo(n-1)+fibo(n-2) #'_' - все остальные (важно)
# print(fibo(int(input())))

# s = [1,2, [3, 4], 5]
# res = []
# def func(lst):
#     for i in lst:
#         if type(i) == list:
#             func(i)
#         else:
#             res.append(i)
# func(s)
# print(res)

# s = [1,2, [3, 4], 's', 5]
# res = []
# p = []

# def func(lst):
#     for i in lst:
#         if type(i) == list:
#             func(i)
#         elif type(i) == int:
#             res.append(i)
#         elif type(i) == str:
#             p.append(i)
# func(s)
# print(res)
# print(p)

# import sys
# print(sys.getrecursionlimit())

# RE Regular expressions

# import re
# s = 'Числа 99, 72, 81, и 999 делятся на 9'
# print(re.findall(r'[7-9]', s)) #- квадратные скобки - от 7 до 9

# import re
# s = 'Числа 99, 72, 81, и 999 делятся на 9'
# print(re.findall(r'[789]', s))

# import re
# s = 'Числа 99, 72, 81, и 999 делятся на 9'
# print(re.findall(r'\d{3}', s)) #- \d[{3} -  ищем 3 цифры

# import re
# s = 'Числа 99, 72, 81, и 999 делятся на 9'
# print(re.findall(r'\d+', s)) #- рядом стощие цифры хотя бы одна

# import re
# s = 'Числа 99, 72, 81, и 999 делятся на 9'
# print(re.findall(r'\d*', s)) #- ищем цифры

# import re
# s = 'Числа 99, 72, 81, и 999 делятся на 9'
# print(re.findall(r'.\d*', s)) #- точка ищет любой символ
# ['Ч', 'и', 'с', 'л', 'а', ' 99', ',', ' 72', ',', ' 81', ',', ' ', 'и', ' 999', ' ', 'д', 'е',

# import re
# s = '12 Числа 99, 72, 81, и 999 делятся на 9'
# print(re.findall(r'..\d*', s)) - ищет по 2 любых символа
#
# ['12', ' Ч', 'ис', 'ла', ' 99', ', 72', ', 81', ', ', 'и 999', ' д', 'ел', 'ят', 'ся', ' н', 'а 9']

# import re
# s = '12 Числа 99, 72, 81, и 999 делятся на 9'
# print(re.findall(r'\d{2}', s)) #- ищет строго 2 цифры
# ['12', '99', '72', '81', '99']

# import re
# s = '12 Числа 99, 72, 81, и 999 делятся на 9'
# print(re.findall(r'\d{2},', s)) #- ищет строго 2 цифры с запятой
# ['99,', '72,', '81,']

#
# import re
# s = '12 Числа 99, 72, 81, и 999 делятся на 9'
# print(re.findall(r' \d{2}', s)) #- ищет строго 2 цифры с запятой
# [' 99', ' 72', ' 81', ' 99']

# import re
# s = '12 Числа 99, 72, 81, и 999 делятся на 9'
# print(re.findall(r'\d, \d', s)) #- ищет строго 2 цифры с запятой
# ['9, 7', '2, 8']

# \w - любая буква
#
# \d+
#
# [+-]?  -- > + - или без них

# print('\\\'') - \'
# print('\'') - '

# в сырых строках (с r вначале) - отключено экранирование

# | - или

# Диапазоны:
# [A-Z] - любой 1 символ от A до Z
#[0-9] - от 0 до 9

# \b - начало или конец
# +- - один или больше элементов
# * - ноль или больше элементов
# ? - ноль или один элемент

# import re
# string = '0abracadabra1'
# regex = r'.a.'
# print(re.findall(regex, string))

# import re
# string = '0abracadabra1'
# regex = r'\da.'
# print(re.findall(regex, string))
# ['0ab']

# import re
# string = '0abracadabra1'
# regex = r'a\d'
# print(re.findall(regex, string))
# ['a1']

# import re
# string = '01 abs 123 456 100 200 cde'
# regex = r'\b1\d\d\b'
# print(re.findall(regex, string))
# ['123', '100']
# \b - начало слова и конец слова

# import re
# string = '01 abs 123 456 1000 200 cde'
# regex = r'\b1\d{3}\b'
# print(re.findall(regex, string))
# ['1000']

# import re
# string = '01 abs 123 456 1000 200 cde'
# regex = r'\b\d{2}\b'
# print(re.findall(regex, string))
# ['01']

# import re
# string = 'Косой косой косил траву на косе'
# regex = r'кос\w*'
# print(re.findall(regex, string))
# ['косой', 'косил', 'косе']

# import re
# string = 'Косой косой косил траву на косе'
# regex = r'кос\w*'
# print(re.findall(regex, string))
# ['косой', 'косил', 'косе']
#
# в + входит и пробел.

# import re
# string = 'Косой косой косил траву на косе покос'
# regex = r'\b\w*кос\w*'
# print(re.findall(regex, string))
# ['косой', 'косил', 'косе']

# import re
# string = 'Косой косой косил траву на косе покос'
# regex = r'\b\w*[Кк]ос\w*'
# print(re.findall(regex, string))
# ['Косой', 'косой', 'косил', 'косе', 'покос']

# import re
# string = 'Косой косой косил траву на косе покос'
# regex = r'\b\w*кос\w*|\b\w*Кос\w*'
# print(re.findall(regex, string))
# ['Косой', 'косой', 'косил', 'косе', 'покос']

# c[a-c]t cat cbt cct
# c[^aui] кроме
#  . - все кроме \n
#
# \d- любая цифра
# \D - любая нецифра
#
# \w - любой символ
# \W - любой несимвол
#
# \s - любой пробельный символ ( и перенос строки и табуляция \t
# \S - любой непробельный символ

# import re
# string = '921-123-4567'
# regex = r'\b\d{3}-\d{3}-\d{4}\b'
# print(re.findall(regex, string))
# ['921-123-4567']

# import re
# string = 'P070TK178 A123BC456'
# regex = r'\b[A-ZА-Я]\d{3}[A-ZА-Я]{2}\d{2,3}\b'
# print(re.findall(regex, string))
# ['P070TK178', 'A123BC456']

# import re
# string = 'Java - самый популярный язык программирования'
# regex1 = r'Java'
# regex2 = r'Python'
# print(re.sub(regex1, regex2, string))
# regex1 - что меняем, regex2 - на что меняем, string - если нигде не найдем

# import re
# string = 'Java - самый популярный язык программирования 2023'
# regex1 = r'2023'
# regex2 = r'2024'
# print(re.sub(regex1, regex2, string))
# Java - самый популярный язык программирования 2024


# import re
# string = 'Java - самый популярный язык программирования 2023'
# regex1 = r'2023'
# regex2 = r'2024'
# print(re.subn(regex1, regex2, string))
# ('Java - самый популярный язык программирования 2024', 1) 1 - кол-во замен

# import re
# string = '(095)6784674 (095)64375564'
# regex1 = r'\(095\)'
# regex2 = r'812'
# print(re.subn(regex1, regex2, string))
# ('8126784674 81264375564', 2)

# import re
# string = '231 3ee 284292 13'
# regex = r'\b\d*[02468]\b'
# print(re.findall(regex, string))

# import re
# string = '231 3ee 284292 13'
# regex = r'\b\d*[05]\b'
# print(re.findall(regex, string))

# * ищет и пустую строку
# + ищет только цифру
#
# import re
# string = '-231 3ee 284292 13'
# regex = r'[+-]?\d+\b'
# lst=re.findall(regex, string)
# print(lst)
# print(sum(list(map(int, lst))))

import re
string = '01 abs 123 456 100 200 cde'
regex = r'\b1\d\d\b'
print(re.findall(regex, string))
