from math import gcd
from functools import reduce
n = list(map(int, input().split()))
nod = reduce(gcd, n)
res = 1
for i in n:
    res *= i
print('NOK =', res // nod)

