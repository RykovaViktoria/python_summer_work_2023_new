import re
s = 'Повторение повторение, ежик ежик ел.'
print(re.sub(r'(\b\w+\b)(\s+\1)+\b', r'\1', s, flags=re.I))



