# def gen():
#     i = 0
#     j = 0
#     while True:
#         i += 1
#         for j in range(i):
#             if i%2==0:
#                 j = i
#                 j *= -1
#             else:
#                 j = i
#         yield j
#
# gener = gen()
# for i in range(int(input())):
#     print(next(gener), end = ',')

def signs():
    i, s = 0, -1
    while True:
        i,s = i + 1, -s
        yield i * s
gen = signs()
for i in range(int(input())):
    print(next(gen), end = ',')