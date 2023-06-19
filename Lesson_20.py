# a = {True:'1',1:'one'}
# print(a)
# {True: 'one'}

# a = {False:'0',0:'zero'}
# print(a)

# import itertools
# for x in itertools.chain([1,2,3],(11,22,'abs'),'abc',{10:100,20:200,30:300}.values()):
#     print(x)
#
# 1
# 2
# 3
# 11
# 22
# abs
# a
# b
# c
# 100
# 200
# 300

# import itertools
# for x in itertools.chain([1,2,3],(11,22,'abs'),'abc',{10:100,20:200,30:300}.items()):
#     print(x)
# 1
# 2
# 3
# 11
# 22
# abs
# a
# b
# c
# (10, 100)
# (20, 200)
# (30, 300)

# import itertools
# s = 'aaabbbbaaaaaddd'
# for k,v in itertools.groupby(s):
#     print(k)
# a
# b
# a
# d

# import itertools
# s = 'aaabbbbaaaaaddd'
# for k,v in itertools.groupby(s):
#     print(*v)
# a a a
# b b b b
# a a a a a
# d d d

# import itertools
# s = 'aaa123bbbbaaaaaddd'
# for k,v in itertools.groupby(s, key = lambda x:x.isdigit()):
#     print(k,*v)
#
# False a a a
# True 1 2 3
# False b b b b a a a a a d d d

# import itertools
# s = [1,2,3,4,5,72]
# for k, v in itertools.groupby(s, key = lambda x: x % 2 ==0):
#     print(k,*v)
#
# False 1
# True 2
# False 3
# True 4
# False 5
# True 72

# import itertools
# def odd(x):
#     return x%2 == 1
# s = [1,23,4,4,76,7]
# for k,v in itertools.groupby(s, key = odd):
#     print(k, '-', *v)
# True - 1 23
# False - 4 4 76
# True - 7

# numpy
# pandas

# import numpy as np
# arr = np.array([5.0,3,2,3,4])
# print(arr.dtype)

# import numpy as np
# lst = [4,5,6]
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(arr.shape)
# [[1 2 3]
#  [4 5 6]]
# (2, 3) - 2 строки, 3 столбца (форма массива)

# import numpy as np
# lst = [4,5,6]
# arr = np.array([[1,2,3],[4,5,6]])
# print(arr*2 + arr)
# [[ 3  6  9]
#  [12 15 18]]

# import numpy as np
# lst = [4,5,6]
# arr = np.array([1,2,3])
# brr = np.array([10,20,30])
# print(arr + brr)
# [11 22 33]

# import numpy as np
# a = np.zeros((2,3), dtype = int)
# print(a)
# b = a.reshape(3,2)
# print(b)
# [[0 0]
#  [0 0]
#  [0 0]]


# import numpy as np
# a = np.ones((4,3), dtype = int)
# print(a)
# b = a.reshape(12)
# print(b)
#
# [1 1 1 1 1 1 1 1 1 1 1 1]


# import numpy as np
# a = np.array([[1,2,3],[10,20,30]])
# np.sum(a,axis =1)
# print(a)

# import numpy as np
# a = np.array([[1,2,3],[10,20,30]])
# print(np.sum(a,axis =1))
#
# [ 6 60]

# import numpy as np
# a = np.array([[1,2,3],[10,20,30]])
# print(np.cbrt(a))
# [[1.         1.25992105 1.44224957]
#  [2.15443469 2.71441762 3.10723251]]

# import numpy as np
# print(np.gcd([6,24,72],[24,36,36]))
# [ 6 12 36]

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linsppace(-2,5,nump=50)
# y=np.exp(x)*100
# plt.plot(x.y)
# plt.grid()

# import numpy as np
# a = np.array([1,2,3,4,5,5,6,7,8,9, np.nan])
# print(np.amax(a))
# print(np.median(a))
# print(np.percentile(a, 25))  - 3.25 - слева от которого 25 % элементов

# import numpy as np
# a = np.array([1,2,3])
# b = np.array([2,2,2])
# print(a == b)
# [False  True False]


# import numpy as np
# a = np.array([1,2,3])
# b = np.array([2,2,2])
# print(a>b)
# [False False  True]

# import numpy as np
# a = np.array([1,2,3])
# condition = a >= 2
# print(a[condition])
# [2 3]

# import numpy as np
# a = np.array([2,7,7,8,8,6])
# condition = a < np.percentile(a, 25)
# print(a[condition])
# print(a[condition])
# [2 6]


# import numpy as np
# x = np.array([2, 7, 7, 8])
# y = np.ones(4) * 100
# a = np.where(x > 5, x, y)
# print(a)
# [100.   7.   7.   8.]

# import numpy as np
# x = np.array([[3,4,5],[3,4,7],[52,6,7]])
# print(x.shape)
# (3, 3)
# print(np.median(x, axis = 0))
# [3. 4. 7.]
# # (3, 3)

# pandas (происх. от панельных данных) panel data

# import pandas as pd
# train_data = pd.read_csv('train.csv')
# train_date.head(10)

# serias - колонки dataframe
# dataframe - плоская двумерная таблица


# import pandas as pd
# df = pd.DataFrame([[1, 'Bob', 'Builder'],
#                   [2, 'Sally', 'Baker'],
#                   [3, 'Scott', 'Master']])
# print(df)
#    0      1        2
# 0  1    Bob  Builder
# 1  2  Sally    Baker
# 2  3  Scott   Master

# import pandas as pd
# df = pd.DataFrame([[1, 'Bob', 'Builder'],
#                   [2, 'Sally', 'Baker'],
#                   [3, 'Scott', 'Master']])
# df.columns = ['##', 'Name', 'Prof']
# df.index = [111,222,333]
# print(df)
#      ##   Name     Prof
# 111   1    Bob  Builder
# 222   2  Sally    Baker
# 333   3  Scott   Master

# import pandas as pd
# df = pd.DataFrame({'country':['RU','KX','BY', 'UA'], 'pop':[1234,2345,3456,4567],'square':[987,876,765,654]})
# df.columns = ['country','population','square'] - изменить название колонки
# print(df)

# import pandas as pd
# df = pd.DataFrame({'country':['RU','KX','BY', 'UA'], 'pop':[1234,2345,3456,4567],'square':[987,876,765,654]})
# df.columns = ['country','population','square']
# df1 = pd.DataFrame()
# lst = {'F':[123,234],'S':[333,444],'T':[444,555]}
# df2 = pd.DataFrame(lst)
# df2['A'] = [111,222]
# df2['X'] = df2['F']+df2['S']
# df2.index = [11,22]
# print(df2)
#       F    S    T    A    X
# 11  123  333  444  111  456
# 22  234  444  555  222  678

# import pandas as pd
# dct = {'Год':[2001,2002,2003,2004,2005],'Товар':['A','B','C','D','E'], 'Шт': [10,20,30,40,50],'Цена':[100,50,30,20,5]}
# df = pd.DataFrame(dct)
# df['Итого']=df['Цена']*df['Шт']
# print(df)
# df.to_excel('test7.xlsx')
# df1 = pd.read_excel('test7.xlsx')
# print(df1)

# import pandas as pd
# dct = {'Год':[2001,2002,2003,2004,2005],'Товар':['A','B','C','D','E'], 'Шт': [10,20,30,40,50],'Цена':[100,50,30,20,5]}
# df = pd.DataFrame(dct)
# df['Итого']=df['Цена']*df['Шт']
# print(df['Шт'])
# print(df.loc[0:2])
#     Год Товар  Шт  Цена  Итого
# 0  2001     A  10   100   1000
# 1  2002     B  20    50   1000
# 2  2003     C  30    30    900

# import pandas as pd
# dct = {'Год':[2001,2002,2003,2004,2005],'Товар':['A','B','C','D','E'], 'Шт': [10,20,30,40,50],'Цена':[100,50,30,20,5]}
# df = pd.DataFrame(dct)
# df['Итого']=df['Цена']*df['Шт']
# print(df['Шт'])
# print(df[(df['Цена'] == 20) | (df['Цена'] == 30)])

# import pandas as pd
# dct = {'Год':[2001,2002,2003,2004,2005],'Товар':['A','B','C','D','E'], 'Шт': [10,20,30,40,50],'Цена':[100,50,30,20,5]}
# df = pd.DataFrame(dct)
# df['Итого']=df['Цена']*df['Шт']
# df.index = [10,20,30,40,50]
# print(df.iloc[0:3])
# iloc - по номеру строки
# loc - по индексу

# import pandas as pd
# dct = {'Год':[2001,2002,2003,2004,2005],'Товар':['A','B','C','D','E'], 'Шт': [10,20,30,40,50],'Цена':[100,50,30,20,5]}
# df = pd.DataFrame(dct)
# df['Итого']=df['Цена']*df['Шт']
# df.index = [10,20,30,40,50]
# df[0:3])

# import pandas as pd
# dct = {'Год':[2001,2002,2003,2004,2005],'Товар':['A','B','C','D','E'], 'Шт': [10,20,30,40,50],'Цена':[100,50,30,20,5]}
# df = pd.DataFrame(dct)
# df['Итого']=df['Цена']*df['Шт']
# df.index = [10,20,30,40,50]
# print(df.T)

# import pandas as pd
# dct = {'Год':[2001,2002,2003,2004,2005],'Товар':['A','B','C','D','E'], 'Шт': [10,20,30,40,50],'Цена':[100,50,30,20,5]}
# df = pd.DataFrame(dct)
# df['Итого']=df['Цена']*df['Шт']
# df.index = [10,20,30,40,50]
# print(df.loc[20, 'Цена'])
# for i in df.index:
#     for j in df.columns:
#         print(i,j, df.loc[i,j])
# 10 Год 2001
# 10 Товар A
# 10 Шт 10
# 10 Цена 100
# 10 Итого 1000
# 20 Год 2002
# и т д

# import pandas as pd
# dct = {'Год':[2001,2002,2003,2004,2005],'Товар':['A','B','C','D','E'], 'Шт': [10,20,30,40,50],'Цена':[100,50,30,20,5]}
# df = pd.DataFrame(dct)
# df['Итого']=df['Цена']*df['Шт']
# df.index = [10,20,30,40,50]
# df1 = df.set_index('Год')
# df1.loc[2002:2003]
# df1.loc[2023] = ['F',100,1,3000]
# for j in df1.columns:
#      print(j, end = ' ')
# print()
# for i in df1.index:
#      print(i, end = ':')
#      for j in df1.columns:
#          print(f'{df1.loc[i,j]:>5}', end = ' ')
#      print()

# import pandas as pd
# dct = {'Год':[2001,2002,2003,2004,2005],'Товар':['A','B','C','D','E'], 'Шт': [10,20,30,40,50],'Цена':[100,50,30,20,5]}
# df = pd.DataFrame(dct)
# df['Итого']=df['Цена']*df['Шт']
# df.index = [10,20,30,40,50]
# print(df.head(2))
# #      Год Товар  Шт  Цена  Итого
# # 10  2001     A  10   100   1000
# # 20  2002     B  20    50   1000
# print(len(df['Товар'].unique()))
# # 5
# print(df.describe())
# #                Год         Шт        Цена        Итого
# # count     5.000000   5.000000    5.000000     5.000000
# # mean   2003.000000  30.000000   41.000000   790.000000
# # std       1.581139  15.811388   36.810325   313.049517
# # min    2001.000000  10.000000    5.000000   250.000000
# # 25%    2002.000000  20.000000   20.000000   800.000000
# # 50%    2003.000000  30.000000   30.000000   900.000000
# # 75%    2004.000000  40.000000   50.000000  1000.000000
# # max    2005.000000  50.000000  100.000000  1000.000000

import pandas as pd
dct = {'Год':[2001,2002,2003,2004,2005],'Товар':['A','B','C','D','E'], 'Шт': [10,20,30,40,50],'Цена':[100,50,30,20,5]}
df = pd.DataFrame(dct)
df['Итого']=df['Цена']*df['Шт']
df.index = [10,20,30,40,50]
print(df['Товар'].value_counts())
# Товар
# A    1
# B    1
# C    1
# D    1
# E    1
print(df+df)
#      Год Товар   Шт  Цена  Итого
# 10  4002    AA   20   200   2000
# 20  4004    BB   40   100   2000
# 30  4006    CC   60    60   1800
# 40  4008    DD   80    40   1600
# 50  4010    EE  100    10    500
