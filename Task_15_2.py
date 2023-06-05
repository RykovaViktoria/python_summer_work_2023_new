import re
s = input('Введите автомобильные номера -->')
# string = 'P070TK178 A123BГ456'
regex = r'\b[ABCEHKMOPTXАВЕКМНОРСТУХ]{3}\d{3}[ABCEHKMOPTXАВЕКМНОРСТУХ]{2}1{0,1}78\b'
print(re.findall(regex, s))
