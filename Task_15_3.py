def mob(s):
    import re
    regex = r'^\+7[(]812[)]\d{3}-\d{4}\b|^\+7[(]921[)]\d{3}-\d{4}\b'
    return re.findall(regex, s)
s = input('Введите телефонные номера -->')
print(mob(s))
