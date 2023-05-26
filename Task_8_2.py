x = [[1,2,3,4], [4555555,5,2], [434,5,23]]
def sort(x):
    return len(str(x)), x.sort(reverse = True)
print(sorted(x, key=sort))


#
# x = [1,2,345]
# len(''.join(map(str, x)))
# print(str(x))