n = int(input('Введите число дисков: '))
def hanoi(n):
    return (n-1)*2+1
print('Минимальное число переустановок = ',hanoi(n))