n = int(input("Введите число -->"))
if n <= 0:
    print('Введите положительное число')
    n = int(input())
    for i in range(1, n+1):
        print(f'{i} x {n} = ', i*n)
else:
    for i in range(1, n+1):
        print(f'{i} x {n} = ', i*n)
