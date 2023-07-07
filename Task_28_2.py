s1 = input('Введите первую строку:')
s2 = input('Введите вторую строку:')

def check(s1,s2):
    return sum([1 for i in range(len(s1)) if s1[i]!=s2[i]])

print(check(s1,s2))
