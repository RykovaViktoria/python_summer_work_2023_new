s = input('Введите строку 1 -->')
d = input('Введите строку 2 -->')
def comp(s,d):
    c = 0
    if len(s)>len(d):
        le = len(s)
        d = d+('0'*(len(s)-len(d)))
    else:
        le = len(d)
        s = s + ('0' * (len(d) - len(s)))
    for i in range(le):
        if s[i]!=d[i]:
            c+=1
        else: pass
    if c > 1:
        return False
    else: return True
print(comp(s,d))