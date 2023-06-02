def tri(n):
    if n == 0:
        print('')
    else:
        print(n*"*")
        tri(n-1)
        print(n*"*")
        return None
n = int(input('Введите натуральное число -->'))
tri(n)
