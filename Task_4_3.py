# import re
# n=input('Введите предложение 1 -->')
# s=input('Введите предложение 2 -->')
# s = re.sub('\s+','', s)
# n = re.sub('\s+','', n)
# reg = re.compile('[^a-zA-Z ]')
# s = reg.sub('', s)
# n = reg.sub('', n)
# print(n ,s)
# print(sorted(list(n))==sorted(list(s)))


# s = input()
# z = input()
# d = {}
# t = {}
# ab = 'abcdefghijklmnopqrstuxvzw'
# ab1 = 'абвгдежз'
# for i in s:
#     if i.lower() in ab or i.lower() in ab1:
#         d[i.lower()] = d.get(i.lower(), 0) + 1
# for i in z:
#     if i.lower() in ab or i.lower() in ab1:
#         d[i.lower()] = d.get(i.lower(), 0) - 1
#
# print(d == t)
print('w'.isalpha())