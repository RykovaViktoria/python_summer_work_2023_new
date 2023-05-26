x = [[1,3,5],[2,4,6],[3,8,9]]
def big(x):
    lst = []
    for i in x:
        # lst.extend(i)
        for j in i:
            lst.append(j)
    print(sorted(sorted(lst, reverse = True)[0:3]))
big(x)

