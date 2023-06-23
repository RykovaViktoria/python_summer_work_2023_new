import keyword
kw = [i.lower() for i in keyword.kwlist]
s = list(('For Our route with math').split())
for n, i in enumerate(s):
    if i.lower() in kw:
        s[n] = '<kw>'
print(' '.join(s))



