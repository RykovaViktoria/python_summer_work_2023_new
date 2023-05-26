def translate(t):
    n = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XC':90,'XL':40,'CD':400,'CM':900}
    s = 0
    for i in t:
        if i in n:
            if t.startswith('IV'):
                s += 4
                t = t.replace("I", "", 1)
                t = t.replace("V", "", 1)
            elif t.startswith('IX'):
                s += 9
                t = t.replace("I", "", 1)
                t = t.replace("X", "", 1)
            elif t.startswith('CM'):
                s += 900
                t = t.replace("C", "", 1)
                t = t.replace("M", "", 1)
            elif t.startswith('CD'):
                s += 400
                t = t.replace("C", "", 1)
                t = t.replace("D", "", 1)
            elif t.startswith('XL'):
                s += 40
                t = t.replace("X", "", 1)
                t = t.replace("L", "", 1)
            elif t.startswith('XC'):
                s += 90
                t = t.replace("X", "", 1)
                t = t.replace("C", "", 1)
            elif t.startswith('IX'):
                s += 90
                t = t.replace("I", "", 1)
                t = t.replace("X", "", 1)
            else:
                s += n[i]
                t = t.replace(i, "", 1)
            if t == "":
                    break
    return s
    print(s)
while True:
    c = input("Введите римское число-->")
    if c == "":
        break
    print(translate(c))
