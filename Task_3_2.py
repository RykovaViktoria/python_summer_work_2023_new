# n=input('Введите число -->')
# for i in range(10):
#     a = n.count(str(i))
#     print(f'{i} - {a}')

x = int(input())
s = str(x)
for i in range(10):
    si = str(i)
    co = 0
    for j in s:
        if j == si:
            co += 1
    print(f'{si} - {co}')