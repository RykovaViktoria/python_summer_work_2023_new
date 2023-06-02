def amount(n):
    if n>9:
        return amount(n // 10) + n%10
    else: return n

n = int(input('Введите натуральное число -->'))
print(amount(n))
