# import functools
# print(functools.reduce(lambda x, y: x * y, [1,2,3,4,5], 100))

# with open("text.txt", 'w') as fo:
#     fo.write('')
# with open("text.txt") as f:
#     print(111, len(f.read()))
#     print(222, len(f.read()))
#
# with open('text.txt', 'r') as fi, open('test.txt', 'w') as fo:
#     for line in fi:
#         print(line)
#         print(line.strip(), file = fo)

# import csv
# columns = ['first_name', 'second_name', 'rating']
# data = [['Иван', 'Иванов', 123], ['Петр', 'Петров', 234]]
# writer = csv.writer(file)
# writer.writerow(columns)
# for row in rows:
#     print(row)


# import csv
# with open('test2.csv', encoding='utf-8') as file:
#     rows = csv.DictReader(file) - создает словарь по столбцам (берет 1ю строку как ключи name salary)
#     su = 0
#     for d in rows:
#         su += int(d['salary'])
#     print(f'ИТОГО: {su}')

# import openpyxl
# wb = openpyxl.load_workbook('excel.xlsx')
# print(wb.sheetnames)
# ws = wb['Данные']
# for i in range(1, ws.max_column + 1):
#     for j in range(1, ws.max_column + 1):
#         c = ws.cell(i,j)
#         if c.value != None:
#             print(c.coordinate, c.value)

# import openpyxl
# wb = openpyxl.load_workbook('excel.xlsx')
# print(wb.sheetnames)
# for sh in wb.sheetnames:
#     ws = wb[sh]
#     print(sh, '________')
#     for i in range(1, ws.max_row + 1):
#         for j in range(1, ws.max_column + 1):
#             c = ws.cell(i,j)
#             if c.value != None:
#                 print(c.coordinate, c.value, end = '/')

# import openpyxl
# wb = openpyxl.load_workbook('excel.xlsx')
# print(wb.sheetnames)
# ws = wb['Данные']
# ws.append({1:'123', 2:'234'})
# wb.save('excel.xlsx')

# import openpyxl
# wb = openpyxl.load_workbook('excel.xlsx')
# print(wb.sheetnames)
# ws = wb['Данные']
# ws.append([1,2,3,4,45,6,3])
# wb.save('excel.xlsx')

# import openpyxl
# print(dir(openpyxl))


# from itertools import permutations
# for i in permutations('abcd', 3):
#     print(i)

# from itertools import permutations
# for i in permutations(['a','b','c','d'], 3):
#     print(i)

# from itertools import permutations
# print(list(map(lambda x: ''.join(x), permutations(['a','b','c','d'], 3))))

# from itertools import permutations
# j = 0
# for i in permutations('abcd', 3):
#     print(i)
#     j +=  1
# print(j)


# from itertools import permutations
# s = 'abcde'
# for r in range(1,6):
#     print(f'{r} - {len(list(permutations(s, r)))}')

# cycle (бесконечно повторяет объект)

# import time
# x = 1000000
# for i in range(0, x, 100000):
#     t0 = time.time()
#     su = 0
#     for j in range(i*10):
#         su += j
#     t1 = time.time()
#     print(i, t1 - t0)

# import time
# time.sleep(5)
# print('r')

# import time
# def f2():
#     t0 = time.time()
#     time.sleep(2)
#     t1 = time.time()
#     return t1 - t0
#
# def f3():
#     t0 = time.time()
#     time.sleep(3)
#     t1 = time.time()
#     return t1 - t0
# s2, s3 = 0,0
# for i in range(11):
#     if i % 2:
#         s3 += f3()
#     else: s2 += f2()
#     print(s2, s3)


# from datetime import datetime
# print(datetime.strptime('24 05 23 20:54', '%d %m %y %H:%M'))

# from datetime import date, time
# my_date = date (2023, 12, 24)
# print(type(my_date))
# my_time = time(21, 0, 0)
# print(type(my_time))
# print(my_date.strftime('%d/%m/%y'), my_time)
# print(my_date.strftime('%A %d, %B %y'), my_time)
# print(my_date.strftime('%a %d, %b %y'), my_time)

# from datetime import datetime
# tdy = datetime.now()
# print('2023-05-24 21:05:59.628016')
# print(tdy)

# from datetime import datetime
# a = datetime(2023, 5, 24, 21, 7, 30)
# print(a.second)

# from datetime import date
# a = date.today()
# print(a)

# import locale
# from datetime import date
# print(locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8'))
# my_date = date(2023, 5, 24)
# print(my_date.strftime('%A %d %B %Y').title())

# import locale
# from datetime import date
# print(locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8'))
# birthday = date(1996, 1, 22)
# print(birthday.strftime('%d %B %A'))

# import locale
# from datetime import datetime
# a = datetime(2023, 5, 24)
# b = datetime(2023, 5, 25)
# c = a - b
# for i in range(10):
#     a += c
#     print(a)
#
# каждый 3й четверг бесплатный вход в Эрмитаже.

# import calendar
# print(calendar.weekday(2023, 5, 24))
# s = calendar.calendar(2023, w=2, l = 1, c = 6, m = 3)
# print(s)

# import calendar
# print(calendar.weekday(2023, 5, 24))

# import calendar
# print(calendar.monthcalendar(2023, 5))

# import calendar
# print(calendar.isleap(1900))

import calendar
year = int(input())
d = {}
for mo in range(1,13):
    month = calendar.monthrange(year, mo)
    for i in range(1, month[1]+1):
        w = calendar.weekday(year, mo, i)
        d[w] = d.get(w, 0) + 1
print(d)





