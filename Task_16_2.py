# import re
# n = input('Введите двузначное число -->')
# s = '44 326'
# n1=str(int(n[0])-1)
# n2=n[1]
# print(n, n1, n2)
# print(re.findall(rf'[0-{n1}][0-9]\D|[{n1}][0-{n2}]\D', s))

#Не работает "или" =(

import re
0 - 9      [0-9]
10 - 19 20-29 3-39 [1-3][0-9]
40 - 45

n = int(input())
x,y = divmod(n,10)
if x == 1 and y ==0:
    regex = rf'(?<!
