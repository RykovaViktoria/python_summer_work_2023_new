import itertools
s = [50,100,200,500,1000,5000]
res = set()
for i in s:
    res.add(i)
for k,v in itertools.permutations(s,2):
    su = k+v
    res.add(su)
for a,b,c in itertools.permutations(s,3):
    su = a+b+c
    res.add(su)
for a,b,c,d in itertools.permutations(s,4):
    su = a+b+c+d
    res.add(su)
for a,b,c,d,e in itertools.permutations(s,5):
    su = a+b+c+d+e
    res.add(su)
tot = sum(s)
res.add(tot)
print(res)

