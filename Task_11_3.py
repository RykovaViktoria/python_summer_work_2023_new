def translate(x):
    s = ''.join((
        ('', 'M', 'MM', 'MMM')[x // 1000 % 10],
        ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')[x // 100 % 10],
        ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')[x // 10 % 10],
        ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')[x % 10]
    ))
    return s
    print(s)

while True:
    n = int(input("Введите арабское число до 3999-->"))
    print(translate(n))
    if n == "":
        break

