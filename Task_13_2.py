# def gen():
#     i = 0
#     s = ''
#     while True:
#         i += 1
#         if str(i)[::1] == str(i)[::-1]:
#             yield i
#         else: pass
#
# gener = gen()
# for i in range(int(input('Введите длину последовательности -->'))):
#     print(next(gener), end = ',')
#

def pal():
    n = 0
    while True:
        n += 1
        if str(n) == str(n)[::-1]:
            yield n
gen = pal()
s = int(input())
while True:
    r = next(gen)
    if r > s: break
    print(r, end = ' ')
