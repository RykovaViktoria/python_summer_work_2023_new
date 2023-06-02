def amount(n):
    if n>9:
        return amount(n // 10) + 1
    else: return 1
n = int(input('Введите натуральное число -->'))
print(amount(n))

