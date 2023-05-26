# f = open("text.txt", 'r', encoding = 'utf-8')
# s = f.readlines()
# # z = f.read(5)
# for i in s:
#     if i.strip() != '':
#         print(i.strip())
# f.close()

# f = open("text.txt", 'r', encoding = 'utf-8')
# s = f.readline()
# print(s.strip())
# z = f.readline()
# print(z.strip())
# f.close()

# f = open("text.txt", 'r', encoding = 'utf-8')
# for i in range(6):
#     s = f.readline()
#     print(s.strip())
# f.close()

# Итерирование файла:
# f = open("text.txt", 'r', encoding = 'utf-8')
# for i in f:
#     print(i.strip())
# f.close()

# f = open("text.txt", 'w', encoding = 'utf-8')
# s = input()
# f.write(s+'\n')
# s = input()
# f.write(s)
# f.close()
# g = open("text.txt", 'r', encoding = 'utf-8')
# s = g.readlines()
# print(s)
# g.close()

# f = open("text.txt", 'w', encoding = 'utf-8')
# s = ['11111\n','222222\n', '33333\n']
# f.writelines(s)
# f.close()
#
# f = open("text.txt", 'r', encoding = 'utf-8')
# s = f.readlines()
# print(*s)
# f.close()

# f = open("text.txt", 'r', encoding = 'utf-8')
# s = f.readlines()
# print(s)
# f.close()
#
# g = open("text9.txt", 'w', encoding = 'utf-8')
#
# for i in s:
#     if set(i) & set('0123456789'):
#         pass
#     else:
#         g.write(i)
#         print(i)
# g.close()

# f = open("text.txt", 'r', encoding = 'utf-8')
# s = f.read()
# print(s)
# f.close()
#
# g = open("text111.txt", 'w', encoding = 'utf-8')
#
# for i in s[::2]:
#     g.write(i)
#     print(i, end = '')
# g.close()
