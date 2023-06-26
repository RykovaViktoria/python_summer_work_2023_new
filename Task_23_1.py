
def odd(s):
    n = len(s)
    h = [0] * n
    C = R = 0      # центр и радиус начала
    opt_i = opt_j = 0     # искомые центр и радиус
    for i in range(n):
        j = 0 if i > C+R else min(h[C-(i-C)], C+R-i)
        while i-j > 0 and i+j < n-1 and s[i-j-1] == s[i+j+1]:
            j += 1
        h[i] = j
        if j > opt_j:
            opt_i, opt_j = i, j
        if i + j > C + R:
            C, R = i, j
    return s[opt_i-opt_j : opt_i+opt_j+1]

def manaker(s):
    return len(odd('|'+'|'.join(s)+'|')[1::2])

print(manaker('aaabbbcccbbbaaafvv'))

