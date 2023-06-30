s = [-2,0,23,1,2,4,5,7,8,99,100]
s.sort()
k = s[0]
lst = []
for i in s[1:]:
    if i - k != 1:
        lst.append(i)
    k=i
print(lst)