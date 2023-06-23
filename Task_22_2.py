d = [(1,2),(1,3),(2,4),(2,5),(3,6),(6,7),(7,8)]
i = 0
lst = []
d.reverse()
lst.append(d[0])
s = d[0][0]
for k,v in d:
    if v == s:
        lst.append(d[i])
        s = k
    i += 1
print('max_len =', len(lst))

