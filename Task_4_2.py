n=int(input('Введите натуральное число -->'))
lst = [[0] * n for i in range(n)]
# for i in range(1, n+1):
#     a = [0]*n
print(lst)
s=0 # счетчик заполнения
for i in range(n):
    s += 1
    lst[i] = s
print(lst)
n = n - 1 # размер столбца после поворота вниз
j = 0 # last value
i = n - 1 # крайний элемент строки
while len(lst)**2 != s:
    for k in range(n):  #движение вниз
        j += 1
        s += 1
        lst[j][i] = s  # заполнение матрицы
    for k in range(n):  #движение влево
        i -= 1
        s += 1
        lst[j][i] = count
print(lst)
#     for k in range(n-1):  #движение вверх
#         j -= 1
#         count += 1
#         a[j][i] = count
#     for k in range(n-1): #движение вправо
#         i += 1
#         count += 1
#         a[j][i] = count
#     n -= 2    # обеспечиваем переход на внутренний виток
# for i in range(len(a)):  #вывод полученной матрицы
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()




