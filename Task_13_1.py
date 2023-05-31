def gen():
    i = 0
    j = 0
    while True:
        i += 1
        for j in range(i):
            if i%2==0:
                j = i
                j *= -1
            else:
                j = i
                j *= 1
        yield j
gener = gen()
for i in range(int(input())):
    print(next(gener), end = ',')