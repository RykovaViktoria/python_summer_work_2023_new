def func(s):
    lst = []
    i=0
    while i < len(s):
        j=''
        while i < len(s) and s[i] in '1234567890':
            j+=s[i]
            i +=1
        i += 1
        lst.append(j)
    lst1 = [int(i) for i in lst]
    # print(lst1)
    ma = max(lst1)
    k = 0
    spi = []
    # print(len(lst1))
    while k <= len(lst1)-2:
        for i in range(0,ma+1):
            if i >= lst1[k] and i <= lst1[k+1]:
                spi.append(i)
            else: pass
        k += 2
    return spi
print(func('1-1,4-6,2-2'))