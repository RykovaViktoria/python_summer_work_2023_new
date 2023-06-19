# import re
# s = input('Введите сочетание слов -->')
# print("".join(re.split(r"\b\s\b", "".join(re.sub(r'\b(\w)\w+\b', r'\1', s.upper())))))

import re
s = input()
print(re.sub(r'\b\w+\b', lambda x:x.group().upper()[0]+str(x.start()), s).replace(' ',''))