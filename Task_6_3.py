s = input()
a = set()
b = set()
c = set()
for i in s:
    if i.isalpha() == True:
        a = set(i) | a
    elif i.isdigit() == True:
        b = set(i) | b
    else: c = set(i) | c
print(f'Буквы - {a}')
print(f'Цифры - {b}')
print(f'Прочие символы - {c}')