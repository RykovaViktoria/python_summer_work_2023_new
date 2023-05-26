n = int(input())
t = []
for i in range(0, n+1):
    t.append([1] + [0]*n)
for i in range(1, n+1):
    for j in range(1,i+1):
        t[i][j]=t[i-1][j]+t[i-1][j-1]
for i in range(0, n+1):
    for j in range(0,i+1):
        print(t[i][j], end = ' ')
    print()












# n = int(input('Введите число -->'))
# f = []
# for i in range(n):
#     f.append([])
#     f[i].append(1)
#     print(f)
#     for k in (1, i):
#         f[i].append(f[i - 1][k - 1] + f[i - 1][k])
#         print(f)
    # if (n != 0):
    #     f[i].append(1)
    # for i in range(n):
    #     print(" " * (n - i), end=" ", sep=" ")
    #     for k in range(0, i + 1):
    #         print('{0:6}'.format(f[i][k]), end=" ", sep=" ")
    #     print()
    #
#
# def f(l):
#     k = 1
#     for i in range(1, l + 1):
#         k = i * k
#     return k
# print(f(9))
#
# n = int(input("-->"))
# for i in range(n + 1):
#     print()
#     for j in range(i + 1):
#         print( int((f(i))/(f(j) * (f(i - j)))), end = " " )


# def str(n):
#     row=list()
#     for i in range(n):
#         if i==0 or i==n-1:
#             row.append(1)
#         else:
#             c_row=str(n-1)
#             row.append(c_row[i-1]+c_row[i])
#     return row
#
# def triangle(m):
#     result=list()
#     for i in range(m):
#         result.append(str(i+1))
#     ### beautify
#     for j in result:
#         print("{:^50s}".format(str(j)))
# triangle(10)







# a = 1
# f = []
# s = 0
# for i in range(0, n):
#     f.append(a)
#     s += f[i]
#     print(s)
#     print(f)
#     if i > 0:
#         f[i] = s
#         f[-i] = s
#     elif i > 2:
#         f[i%2] = s + 2
#



        #print(f)
    # elif i > n: break



# f[i] += s

# n = int(input('Введите число -->'))
# f = []
# for i in range(n):
#     f += [1]
#     print(f)
#     for i in range(1, len(f)-1):
#         f[i] += f[i+1]
#     print(f)

# num = int(input("Enter the number: "))
# list1 = [] #an empty list
# for i in range(num):
#   list1.append([])
#   list1[i].append(1)
#   for j in range(1, i):
#     list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
#   if(num != 0):
#     list1[i].append(1)
# for i in range(num):
#   print(" " *(num - i), end = " ", sep = " ")
#   for j in range(0, i + 1):
#     print('{0:6}'.format(list1[i][j]), end = " ", sep = " ")
#   print()
# Источник: https://pythonpip.ru/examples/programma-python-dlya-pechati-treugolnika-paskalya

