alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = list(map(str, input('Введите строку латинскими буквами -->')))
n = int(input('Введите величину сдвига -->'))
def code(s, n):
    str = ''
    for i in s:
        str += alphabet[(alphabet.index(i) + n) % len(alphabet)]
    print('Code:', str)
code(s,n)