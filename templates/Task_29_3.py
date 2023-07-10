s = input('Введите первую строку: ')
w = input('Введите вторую строку: ')
def func(s,w):
    su = {}
    wu = {}
    c = 1
    b = 1
    lst1 = []
    lst2 = []
    for i in s:
        su[i]=c
        c+=1
    for i in w:
        wu[i]=b
        b+=1
    if len(s)==len(w):
        for i in su:
            lst1.append(su[i])
        for i in wu:
            lst2.append(wu[i])
        if lst1==lst2:
            return True
        else: return False
    else: return False
print(func(s,w))



