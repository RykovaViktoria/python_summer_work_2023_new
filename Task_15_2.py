# import re
# s = input('Введите автомобильные номера -->')
# # string = 'P070TK178 A123BГ456'
# regex = r'\b[ABCEHKMOPTXАВЕКМНОРСТУХ]{3}\d{3}[ABCEHKMOPTXАВЕКМНОРСТУХ]{2}1{0,1}78\b'
# print(re.findall(regex, s))

# import re
# a = 'AАBВCСXХYУ'
# regex = rf'[{a}]\d\d\d[{a}][{a}][1]?78'
# s = input()
# print(re.findall(regex, s))

import re
regex = r'[AABB]\d{3}[AABB]{2}[1]?78'
s = input()
print(re.findall(regex, s))

