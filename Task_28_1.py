import itertools
lst = [5,4,3,2,1]

def co(lst):
    c = 0
    for k,v in itertools.combinations(lst,2):
        a = lst.index(k)
        b = lst.index(v)
        if a<b and k>v:
            c+=1
    return c
print(co(lst))
