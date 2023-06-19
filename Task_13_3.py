# def sum_list(lst):
#     lst1 = []
#     i = 0
#     while True:
#         if i >= len(lst):
#             return
#         elif lst[i] % 2 == 0: pass
#         else: lst1.append(lst[i])
#         yield lst1
#         i += 1
#
# lst = list(map(int,input('Введите числа через пробел -->').split()))
# gen_sum = sum_list(lst)
# for _ in range(len(lst)):
#     res = []
#     res += next(gen_sum)
# print(res)

def odds(lst):
    for i in lst:
        if i % 2:
            yield i
lst = list(map(int, input().split()))
gen = odds(lst)
for i in gen:
    print(i, end = ' ')
