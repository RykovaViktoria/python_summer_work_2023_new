import re
s = input('Введите сочетание слов -->')
print("".join(re.split(r"\b\s\b", "".join(re.sub(r'\b(\w)\w+\b', r'\1', s.upper())))))