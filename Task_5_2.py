# n = int(input())
# f=[]
# for i in range(1, n+1):
#     if n % i ==0:
#         f.append(i)
#     else: None
# print(f)
# s = []
# for i in f:
#     c=0
#     for j in range(1, i+1):
#         if i%j==0:
#
n = int(input())
for i in range(2,n+1):
    hm=0
    while n % i == 0:
        hm += 1
        n //= i
    if hm:
        print(f'{i=}-{hm}')
    if n == 1:
        break








