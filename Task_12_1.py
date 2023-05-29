def spi(x):
    ma = max(x)
    mi = min(x)
    lst1 = [i for i in range(len(x)) if x[i] == ma]
    lst2 = [i for i in range(len(x)) if x[i] == mi]
    return lst1, lst2
print(spi([1,2,3,3,1]))