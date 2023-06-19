# .* -  жадный поиск
# .*? - линивый поиск

# import re
# print(re.findall(r'Isaac\d (?=Asimov)', 'Isaac1 Asimov, Isaak2 other'))
# ['Isaac1 ']
# там где совпало

# import re
# print(re.findall(r'Isaac\d (?!Asimov)', 'Isaac1 Asimov, Isaak2 other'))

# (?<=-)  --> искать все числа перед которыми стоит минус

# import re
# z = input('Введите подслово:')
# print(*re.findall(rf'\b\w+{z}\w+\b', 'косой косил коса покос'))
# * - выводит слова через пробел, а не списком.

# import time
# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.perf_counter()
#         val = func(*args,**kwargs)
#         end = time.perf_counter()
#         work_time = end - start
#         print(func.__name__, work_time)
#         return val
#     return wrapper
# @timer
# def sleep(n): time.sleep(n)
# print(sleep(4))
# @timer
# def test(n):
#     return sum([(i/99)**2 for i in range(n)])
# print(sleep(1))
# print(test(100000))
# dubble underscore (__) name - скрытая функция

# def deco(func):
#     def wrapper(*args,**kwargs):
#         res = ''.join(args)
#         func(*args,**kwargs)
#         return res
#     return wrapper
# @deco
# def test(*args):
#     pass
# @deco
# def test2():
#     pass
# print(test('аргумент1','аргумент2','аргумент3'))
# print(test2())

#Декоратор - логирование ошибок в файл
# import time
# def deco(func):
#     def wrapper(*args, **kwargs):
#         with open('log.txt', 'a', encoding = 'utf-8') as f:
#             print(time.ctime(), func.__name__, 'Start', file = f)
#         try:
#             func(*args, **kwargs)
#         except Exception as e:
#             with open('log.txt', 'a', encoding = 'utf-8') as f:
#                 print(time.ctime(), func.__name__, '!!!', e, file = f)
#             print(time.ctime(), func.__name__, '!!!', e)
#         return
#     return wrapper
# @deco
# def sleep(n):
#     time.sleep(n)
# sleep(2)
# @deco
# def test():
#     print(1/0)
# sleep(2)
# test()

# __ - дамбер
# экземпляр или объект или инстанс (синонимы)
# class Person:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#     def give_money(self, other, x_money):
#         self.money -= x_money
#         other.money += x_money
#
# a = Person('Pete', 200)
# print(a.name)
# print(a.money)
# b = Person('Nick', 300)
# print(b.name, b.money)
# a.give_money(b, 100)
# b.give_money(a, 100)
# print(a.money, b.money)
#скотный двор (антиутопия)
# class Person:
#     def __init__(self, name, money): #self - кто стоит до вызова метода ( a или b)
#         self.name = name
#         self.money = money
#     def give_money(self, other, x_money):
#         self.money -= x_money
#         other.money += x_money
#     def equal(self, other):
#         x = (self.money + other.money)/2
#         self.money = x
#         other.money = x
#
# a = Person('Pete', 200)
# b = Person('Nick', 300)
# a.equal(b)
# print(a.money, b.money)
#
# 250.0 250.0

# class Person:
#     def __init__(self, name, money, interest = 10): #self - кто стоит до вызова метода ( a или b)
#         self.name = name
#         self.money = money
#         self.interest = interest
#     def give_money(self, other, x_money):
#         self.money -= x_money
#         other.money += x_money
#         self.info()
#         other.info()
#     def equal(self, other):
#         x = (self.money + other.money)/2
#         self.money = x
#         other.money = x
#         self.info()
#         other.info()
#     def info(self):
#         print(f'{self.name} has ${self.money}')
#     def income(self, years):
#         for i in range(1, years +1):
#             self.money = self.money * (1+self.interest/100)
#             print(f'{i} year = {self.money}')
#         self.info()
#
# a = Person('Pete', 100, 5)
# b = Person('Nick', 300, 7.5)
# b.income(10)
# a.income(10)


# class Person:
#     def __init__(self, name, money, interest = 10): #self - кто стоит до вызова метода ( a или b)
#         self.name = name
#         self.money = money
#         self.interest = interest
#     def give_money(self, other, x_money):
#         if self.money < x_money:
#             print('Денег мало')
#         else:
#             self.money -= x_money
#             other.money += x_money
#         self.info()
#         other.info()
#     def equal(self, other):
#         x = (self.money + other.money)/2
#         self.money = x
#         other.money = x
#         self.info()
#         other.info()
#     def info(self):
#         print(f'{self.name} has ${self.money}')
#     def income(self, years):
#         for i in range(1, years +1):
#             self.money = self.money * (1+self.interest/100)
#             print(f'{i} year = {self.money}')
#         self.info()
#
# a = Person('Pete', 100, 5)
# b = Person('Nick', 300, 7.5)
# a.give_money(b, 200)
# # Денег мало
# # Pete has $100
# # Nick has $300
#
# class Teacher(Person): # Наследование
#     pass
# c = Teacher('Jack', 1000)
# c.info()
# # Денег мало
# # Pete has $100
# # Nick has $300
# # Jack has $1000

class Pet:
    def __init__(self, name, weight, level_of_fullness):
        self.name = name
        self.weight = weight
        self.level_of_fullness = level_of_fullness
    def info(self):
        print(f'{self.name} has weight={self.weight} and he satiated {self.level_of_fullness}')
    def hungry(self):
        if self.level_of_fullness < 5:
            print('hungry')
        else:
            print('fullness')
    def feed(self):
        self.level_of_fullness += int(input())

a = Pet('cat', 4, 0)
a.feed()
a.hungry()
a.info()

