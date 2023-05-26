# s = "АГЦТАААГГГГГГГГГГГГЦЦТ"
# def c(s, n):
#     d = {}
#
#     for i in range(len(s) - n + 1):
#         if s[i] not in d:
#             d[s[i:i + n]] = 1
#             print(d)
#         d[s[i: i + n]] += 1
#     ma = max(d.values())
#     return ma, d
# print(c(s, 3))

# s = 'АГЦТТФГЦЦ'
# def repeat(s, n):
#     d = {}
#     for i in range(len(s)-n+1):
#         d[s[i:i+n]]=d.get(s[i:i+n], 0) + 1
#     ma = max(d.values())
#     res = []
#     for k, v in d.items:
#         if v == ma:
#             res.append(k)
#     return res
# print(repeat(s,3))

# s1 = "АГТЦТЦАГЦТ"
# s = list(s1)
# for i in range(len(s) - 1):
#     if (s[i] == "А" and s[i + 1] == "Г") or (s[i] == "Г" and s[i + 1] == "А"):
#         s[i], s[i + 1] = s[i + 1], s[i]
# st = ""
# for i in s:
#     st += i
# s3 = ""
# for i in range(len(st)):
#     if (st[i:].startswith("ТЦ") == True) or (st[i:].startswith("ЦТ") == True):
#         s3 += s[i] + "АГ"
#     else:
#         s3 += st[i]
# print(s3)

s = input() # АГГЦФТЦ ГААГТАГЦ
z =''
i = 0
while True:
    if s[i:i+2] == 'АГ':
        z += 'ГА'
        i += 2
    elif s[i:i+2] == 'ЦТ':
        z += 'ЦАГТ'
        i += 2
    else:
        z += s[i]
        i += 1
    if i >= len(s) - 1: break
print(z)