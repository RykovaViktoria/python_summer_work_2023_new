import re
n = input('Введите двузначное число -->')
s = '44 326'
n1=str(int(n[0])-1)
n2=n[1]
print(n, n1, n2)
print(re.findall(rf'[0-{n1}][0-9]\D|[{n1}][0-{n2}]\D', s))

#Не работает "или" =(
