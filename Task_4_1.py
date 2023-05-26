n=input('Введите выражение -->')
lst = n.split()
x=lst[0]
y=lst[2]
op=lst[1]
if y == '0' and op == '/':
    print('Делить на 0 нельзя. Введите другой знаменатель.')
    n = input('Введите выражение -->')
else:
    s=compile(f'{x}{op}{y}', 'test', 'eval')
    print(f'{x} {op} {y} = ',  eval(s))



