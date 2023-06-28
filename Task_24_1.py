s = [5,3,2,6,0,4,73,34]
def maxi(s):
    k = 0
    for i in s:
        if k < i:
            k = i
    return k

def sor(s):
    lst = []
    c = s.copy()
    while len(c) != 0:
        for i in s:
            if i == maxi(c):
                lst.append(i)
                c.pop(c.index(i))
    return lst
print(sor(s))




