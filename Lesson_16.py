# ? - ноль или один элемент

# [^] -кроме
# ^ - начало текста
# $ - конец текста
#
# import re
# text = 'ABCfizz.123.buzz.456.fizzbuzz'
# res1 = re.sub(r'\d+',r'#', text)
# res2 = re.sub(r'[a-z]+',r'(*)', text)
# print(res1)
# print(res2)

import re
# def fullname(x):
#     s = x.group()
#     print(x.group(), x.start(), x.end())
#     if s == 'Коля': return 'Николай'
#     elif s == 'Миша': return 'Михаил'
#     elif s == 'Даня': return 'Даниил'
#
#
# text = 'Здравствуй, Коля! Привет, Миша! Даня'
# print(re.sub(r'\b\w{4}\b', fullname, text))
# Коля 12 16
# Миша 26 30
# Даня 32 36
# Здравствуй, Николай! Привет, Михаил! Даниил

# import re
# def fullname(x):
#     s = x.group()
#     print(x.group(), x.start(), x.end())
#     if s == 'LED': return 'Пулково'
#     elif s == 'MSQ': return 'Минск'
#     elif s == 'SVO': return 'Шереметьево'
#     elif s == 'SVX': return 'Кольцово'
#     else: return s
#
# text = 'LED MSQ SVO SVX'
# print(re.sub(r'\b\w{3}\b', fullname, text))
# LED 0 3
# MSQ 4 7
# SVO 8 11
# SVX 12 15
# Пулково Минск Шереметьево Кольцово

# import re
# text = 'first second'
# print(re.sub(r'(first) (second)', r'\2 \1', text))
# second first

# import re
# text = 'first second free split'
# print(re.sub(r'(f\w*) (s\w*)', r'\2 \1', text))
# second first split free

# import re
# text = 'Илон Маск Андреевич'
# print(re.sub(r'(\w+) (\w+) (\w+)', r'\2 \3 \1', text))
# Маск Андреевич Илон

# import re
# text = 'ф И О Ф И О Ф И О'
# print(re.sub(f'Ф', 'Иванов',  text, count  =2, flags = re.I))

# import re
# text = '123 first 234 second'
# print(re.findall(r'(\d+) \w+', text))
# ['123', '234']

# import re
# text = '123 = first 234 = second'
# print(re.findall(r'(\d+) (=) (\w+)', text))
# [('123', '=', 'first'), ('234', '=', 'second')

# import re
# text = '123:first 234:second'
# print(re.findall(r'(\d+):(\w+)', text))
# [('123', 'first'), ('234', 'second')]

# import re
# text = 'www.itmo.ru www.fr.fr'
# print(re.findall(r'www.(\w+).(?:ru|com|by)', text))
# ['itmo']

# import re
# text = 'abracadabra'
# res = re.finditer(r'ab', text)
# for i in res:
#     print(i.group(), i.start(), i.end())
# ab 0 2
# ab 7 9

# import re
# text = 'abracadabra'
# res = re.finditer(r'[^a]', text)
# for i in res:
#     print(i.group(), i.start(), i.end())

# import re
# def fun(x):
#     return 'A'+str(x.start())
# text = 'abracadabra'
# res = re.sub(r'a', fun, text)
# print(res)

# A0brA3cA5dA7brA10

# import re
# from collections import Counter
# text = 'ванна питон папа роща'
# s = re.findall(r'\b\w+\b', text)
# print(s)
# for i in s:
#     if max(Counter(i).values())>1:
#         print(i)
# ванна
# папа

# import re
# text = '1     +    22222   *  3    - 7 / 2'
# print(re.split(r'[0-9]+', text))
# ['', '     +    ', '   *  ', '    - ', ' / ', '']

# import re
# text = 'www.itmo.ru'
# print(re.split(r'[.]', text))
# ['www', 'itmo', 'ru']

# Разюбить текст по символам
# import re
# text = 'Отлично!Отлично?отлично;точка.запятая,все'
# print(re.split(r'[.,:;!?]', text))
# ['Отлично', 'Отлично', 'отлично', 'точка', 'запятая', 'все']

# import re
# numb = re.compile(r'\d+')
# print(re.findall(numb, 'aaa 111 sdd 123 ccc'))
# print(numb.findall('aaa 111 sdd 123 ccc'))
# ['111', '123']
# ['111', '123'] Одно и то же

# import re
# x = 5
# print(re.findall(fr'{x}', '1235242'))
# ['5']

# import re
# x = 5
# print(re.findall(fr'{str(x)*2}', '12355242'))

# import re
# x = 5
# res = '|'.join(str(i) for i in range(x))
# print(re.findall(fr'{res}', '11122233345'))
# print(res)
# ['1', '1', '1', '2', '2', '2', '3', '3', '3', '4']
# 0|1|2|3|4

# Декораторы

# def func(f):
#     return f
# def hello():
#     print('Hello')
# hello()
# func(hello)()
# def bye():
#     print('GoodBye')
# func(bye)()
# Hello
# Hello
# GoodBye

# def speak(text):
#     def whisper(t):
#         return t.lower()
#     return whisper(text)
# print(speak('Hello'))
# hello

# def speak(text):
#     def whisper(t):
#         return t.lower()
#     return whisper
#
# s = speak('Hello World')
# print(s('DDDD'))
# print(s)
# <function speak.<locals>.whisper at 0x10d197880>

# def speak(text):
#     def whisper():
#         print(text.lower())
#     return whisper
#
# s = speak('Hello World')
# r = speak('Welcome')
# r()
# welcome

# Простейший декоратор
# def null_deco(func):
#     return func
# def hello():
#     print('Hello world')
#
# hello = null_deco(hello)
# hello()

# def sample_deco(func):
#     def wrapper():
#         print('Начало функции')
#         func() #- уже существует до декоратора или ее можно написать в процессе
#         print('Конец функции')
#     return wrapper
#
# def say():
#     print('Hello world')
# say = sample_deco(say)
# say()

# def sample_deco(func):
#     def wrapper():
#         print('Начало функции')
#         func() #- уже существует до декоратора или ее можно написать в процессе
#         print('Конец функции')
#     return wrapper
# @sample_deco
# def say():
#     print('Hello world')
# say()
# Начало функции
# Hello world
# Конец функции

# def sample_deco(func):
#     def wrapper():
#         result = func()
#         new_res = result.upper()
#         return new_res
#     return wrapper
# @sample_deco
# def say():
#     return 'Hello world'
# print(say())

def sample_deco(func):
    def wrapper():
        result = func()
        new_res = ' '.join(result.split()[::-1])
        return new_res
    return wrapper
@sample_deco
def say():
    return 'Hello world'
@sample_deco
def talk():
    return 'Goodbye'
print(say() + ' ' + talk())

world Hello Goodbye

