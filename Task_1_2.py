x, y = int(input("Введите число -->")), int(input("Введите число -->"))
a = x + y
b = x - y
c = x * y
d = x / y
e = x // y
list=[a,b,c,d,e]
list.sort()
print(list)
print('Наибольшее число:', list[-1])