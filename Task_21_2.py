import numpy as np
x = np.array([[3,4,5,4],[3,4,7,2],[52,6,7,2]])
print(x)
lst =[]
lst.append(x[0][0])
a = len(x)
b = len(x[0])
i = 0
j = 0
while a-1 > i and b-1 > j:
    if x[i][j+1] < x[i+1][j]:
        lst.append(x[i][j+1])
        i = i
        j =+ 1
    else:
        lst.append(x[i+1][j])
        i += 1
        j = j

print(' + '.join(map(str, lst)), '=', sum(lst))

