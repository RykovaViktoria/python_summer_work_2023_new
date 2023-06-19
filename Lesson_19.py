# Прикидываем структуру данных:
# class Teacher:
#     def task(self):
#         s = input('Введите новую задачу:')
#     def check(self):
#         pass
#
# class Pupil:
#     pupil_list = []
#     def __init__(self, name):
#         self.name = name
#         Pupil.pupil_list.append(self)
#     def solution(self):
#         pass
import itertools

# class Student:
#     stdnt = []
#     def __init__(self, name, fivers, tens, twenties):
#         self.name = name
#         self.fivers = fivers
#         self.tens = tens
#         self.twenties = twenties
#         Student.stdnt.append(self)
# a = Student('a',0,0,0)
# b = Student('b', 1, 1, 1)
# c = Student('c',2,2,2)
# print(Student.stdnt)
# for i in Student.stdnt:
#     print(i.name)
#
#
# class Student:
#     stdnt = []
#     def __init__(self, name, fivers, tens, twenties):
#         self.name = name
#         self.fivers = fivers
#         self.tens = tens
#         self.twenties = twenties
#         Student.stdnt.append(self)
#     def money(self):
#         return self.fivers*5+self.tens*10+self.twenties*20
# a = Student('a',0,0,0)
# b = Student('b', 1, 1, 1)
# c = Student('c',2,2,2)
# print(Student.stdnt)
# for i in Student.stdnt:
#     print(i.name, i.money())
#

# class D:
#     def __init__(self):
#         self.__a = 123
#
# dd = D()
# print(dd._D__a)


# class D:
#     def __init__(self):
#         self.__a = 123
#     def get_a(self):
#         return self.__a
#
# dd = D()
# print(dd._D__a)
# print(dd.get_a())
# 123
# 123

# class Person:
#     instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.instance:
#             cls.instance = object.__new__(cls)
#         return cls.instance
#     def __init__(self):
#         self.name = 'Peter'
# obj_one = Person()
# obj_two = Person()
# print(obj_one is obj_two)
# True


# class Person:
#     '''Документация Person'''
#     def show(self):
#         '''Документация show'''
# t = Person()
# print(t.__doc__)
# print(Person.__doc__)
# print(t.show.__doc__)
# Документация Person
# Документация Person
# Документация show

# class Car:
#     def __init__(self, model, color, vin):
#         self.model = model
#         self.color = color
#         self.vin = vin
#     def __str__(self):
#         return f'Модель:{self.model} с VIN {self.vin}'
#     def __repr__(self):
#         return f'{self.model}, {self.color}, {self.vin}'
# car = Car('Merc', 'silver', 'WDB123456789')
# print(car)
# print(str(car))
# print(repr(car))
#
# repr рекомендуется

# class Car:
#     def __init__(self, model, color, vin):
#         self.model = model
#         self.color = color
#         self.vin = vin
#     def __str__(self):
#         return f'Модель:{self.model} с VIN {self.vin}'
#     def __repr__(self):
#         return f'{self.model}, {self.color}, {self.vin}'
# car = Car('Merc', 'silver', 'WDB123456789')
# print(car.__dict__)
# for k,v in car.__dict__.items():
#     print(k,v)
#
# {'model': 'Merc', 'color': 'silver', 'vin': 'WDB123456789'}
# model Merc
# color silver
# vin WDB123456789

# class Car:
#     def __init__(self, model, color, vin):
#         self.model = model
#         self.color = color
#         self.vin = vin
#     def __str__(self):
#         return f'Модель:{self.model} с VIN {self.vin}'
#     def __repr__(self):
#         return f'{self.model}, {self.color}, {self.vin}'
# car = Car('Merc', 'silver', 'WDB123456789')
# print(car.__dict__)
# car.__dict__['price']=12345
# for k,v in car.__dict__.items():
#     print(k,v)
# print(car.price)
# car2 = Car('m', 'c', 'v')
# print(car2)
# Car.price = 999999
# print(car.price)
# print(car2.price)
#
# /Users/viktoriapavlova/PycharmProjects/python_summer_work_2023/venv/bin/python /Users/viktoriapavlova/PycharmProjects/python_summer_work_2023/Lesson_19.py
# {'model': 'Merc', 'color': 'silver', 'vin': 'WDB123456789'}
# model Merc
# color silver
# vin WDB123456789
# price 12345
# 12345
# Модель:m с VIN v
# 12345
# 999999

#
# Переопределите метод car, чтобы печатались все атрибуты и их значения через запятую
# class Car:
#     def __init__(self, model, color, vin):
#         self.model = model
#         self.color = color
#         self.vin = vin
#     def __str__(self):
#         return ','.join(str(i)+':'+str(j) for i,j in self.__dict__.items())
#     def __repr__(self):
#         return f'{self.model}, {self.color}, {self.vin}'
# car = Car('Merc', 'red', 'VIN123')
# print(car)
#
# model:Merc,color:red,vin:VIN123


# class Car:
#     def __init__(self, model, color, vin):
#         self.model = [1,2,3]
#         self.color = color
#         self.vin = vin
#     def __str__(self):
#         return ','.join(str(i)+':'+str(j) for i,j in self.__dict__.items())
#     def __repr__(self):
#         return f'{self.model}, {self.color}, {self.vin}'
# car = Car('Merc', 'red', 'VIN123')
# print(car)

# model:[1, 2, 3],color:red,vin:VIN123
#
# Равенство значений объектов класса eq

# class Car:
#     def __init__(self, model, color, vin):
#         self.model = [1,2,3]
#         self.color = color
#         self.vin = vin
#     def __eq__(self, other):
#         return self.vin == other.vin and self.model == other.model and self.color == other.color
# car1 = Car('Merc','red','VIN123')
# car2 = Car('Merc', 'black', 'VIN123')
# print(car1==car2)
# False


# class Car:
#     def __init__(self, model, price):
#         self.model = model
#         self.price = price
#     def __gt__(self, other):
#         return int(self.price) > int(other.price)
#
# car1 = Car('Merc', '5000')
# car2 = Car('Merc', '4000000')
# print(car1 > car2)


# class StrStr:
#     def __init__(self, string):
#         self.n = string
#     def __gt__(self, other):
#         return len(self.n) > len(other.n)
# a = StrStr('aaa')
# b = StrStr('bbbbbbb')
# print(min(a,b).n)
# aaa
#

# class Student:
#     stdnt = []
#     def __init__(self, name, fivers, tens, twenties):
#         self.name = name
#         self.fivers = fivers
#         self.tens = tens
#         self.twenties = twenties
#         Student.stdnt.append(self)
#     def money(self):
#         return self.fivers*5+self.tens*10+self.twenties*20
#     def __lt__(self, other):
#         return self.money() < other.money()
# a = Student('aaa',100,0,0)
# b = Student('bbb', 1, 1, 1)
# c = Student('ccc',2,2,2)
# print(min(a,b,c).name)
# print(max(a,b,c).name)
# print(*dir(a))
# print(min(Student.stdnt).name)

# class Plus:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Plus(self.x+other.x, self.y+other.y)
#     def __str__(self):
#         return f'Plus({self.x}, {self.y})'
# a = Plus(1,2)
# b = Plus(10,20)
# print(a+ b)
# Результат: Plus(11, 22)

# уравнение прямой
# class LineGen:
#     def __init__(self, k, b):
#         self.k = k
#         self.b = b
#     def __call__(self, x):
#         return self.k*x + self.b
# lf1 = LineGen(2,5)
# lf2 = LineGen(-6, 9)
# print(lf1(10))
# print(lf2(4))
# 25
# -15

# num = [1,2,3]
# it = iter(num)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# num = [1,2,3]
# print(*dir(num))

# num = [1,2,3]
# it = iter(num)
# print(*dir(it))

# Собственный итератор
# class SI:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             raise StopIteration
# s_iter = SI(3)
# print(next(s_iter))
# print(next(s_iter))
# print(next(s_iter))

# class SI:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return self.counter
#         else:
#             raise StopIteration
#     def __iter__(self):
#         return self
# s_iter = SI(3)
# for i in s_iter:
#     print(i)

# class Fact:
#     def __init__(self, limit):
#         self.value = 1
#         self.index = 1
#         self.limit = limit
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.value *= self.index
#         if self.index > self.limit:
#             raise StopIteration
#         self.index +=1
#         return self.value
# f = Fact(5)
# for i in f:
#     print(i)
#     input()
#
# 1
#
# 2
#
# 6
#
# 24
#
# 120

# class Fact:
#     def __init__(self, limit):
#         self.value = 0
#         self.index = 1
#         self.limit = limit
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.value += self.index
#         if self.index > self.limit:
#             raise StopIteration
#         self.index +=1
#         return self.value
# f = Fact(5)
# for i in f:
#     print(i)
#     input()
#
# 1
#
# 3
#
# 6
#
# 10
#
# 15

# itertools.combinations - сочетания
# itertools.combinations_with_replacement - сочетания c повторами
#
# itertools.cycle - бесконечно раз повторяет
# itertools.chain - принимает любые объекты

# import itertools
# s = input()
# res = set()
# for i in itertools.permutations(s):
#     res.add(''.join(i))
# print(res)
# sf
# {'fs', 'sf'}


class Student:
    stdnt = []
    def __init__(self, name, fivers, tens, twenties):
        self.name = name
        self.fivers = fivers
        self.tens = tens
        self.twenties = twenties
        Student.stdnt.append(self)
    def money(self):
        return self.fivers*5+self.tens*10+self.twenties*20
    def __lt__(self, other):
        return self.money() < other.money()
a = Student('aaa',10,0,0)
b = Student('bbb', 1, 1, 1)
c = Student('ccc',2,2,2)
for i in sorted(Student.stdnt):
    print(i.name, i.money())

bbb 35
aaa 50
ccc 70