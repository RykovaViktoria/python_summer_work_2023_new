import re
s = input('Введите телефонные номера -->')
regex = r'^\+7[(]812[)]\d{3}-\d{4}\b|^\+7[(]921[)]\d{3}-\d{4}\b'
print(re.findall(regex, s))
