s = list(input())
d = {}
d1 = d.fromkeys(s, None)
d0 = {'G':'C','C':'G','T':'A','A':'T'}
w = ''
for k, v in d1.items():
    v = d0.setdefault(k)
    w += v
print(w)


for i in dnk:

