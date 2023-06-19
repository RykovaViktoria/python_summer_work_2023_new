# dct = {1:11,2:{1:111,2:222,3:{0:33,3:333}}}
# n = int(input('Введите число -->'))
# spi = []
# def val(d, n):
#     for k, v in d.items():
#         if type(v) == dict:
#             if k == n:
#                 spi.append(v)
#             val(v, n)
#         elif k == n:
#             spi.append(v)
#
# val(dct, n)
# print(spi)

dct = {1:11,2:{1:111,2:222,3:{0:33,3:333}}}
def fu(dct,x):
    r = []
    for k,v in dct.items():
        print(r,k,v)
        if k ==x:
            r.append(v)
        if type(v) == dict:
            r.extend(fu(v, x))
    print(r)
    return r
x = int(input())
print(fu(dct, x))

