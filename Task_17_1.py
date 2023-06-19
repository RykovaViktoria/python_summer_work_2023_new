import re
s = 'aaa aaab'
print(re.sub(r'(\b\w+\b)(\s+\1)+\b', r'\1', s, flags=re.I))



