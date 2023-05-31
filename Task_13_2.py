def gen():
    i = 0
    s = ''
    while True:
        i += 1
        if str(i)[::1] == str(i)[::-1]:
            yield i
        else: pass

gener = gen()
for i in range(int(input('Введите длину последовательности -->'))):
    print(next(gener), end = ',')

