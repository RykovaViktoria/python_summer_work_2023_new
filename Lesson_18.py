# class Shape:
#     x = 123
#     def __init__(self, color, square=10):
#         self.color = color
#         self.square = square
#     def get_color(self):
#         return self.color
#     def set_color(self, new_color):
#         self.color = new_color
#
# a = Shape('Red')
# print(a.x)
# a.x = 234
# print(a.x)
# b = Shape('Green')
# print(b.x)

# class Shape:
#     x = []
#     def __init__(self, color, square=10):
#         self.color = color
#         self.square = square
#         self.lst = [1,2,3]
#     def get_color(self):
#         return self.color
#     def set_color(self, new_color):
#         self.color = new_color
#
# a = Shape('Red')
# print(a.lst)

# ДО было процедурное/последовательное/структурное программирование
# а теперь: ООП

# class Figure:
#     def __init__(self, perimeter, color='black'): #сначала позиционный, потом именованный аргумент
#         self.color = color
#         self.perimeter = perimeter
#     def get_perimeter(self):
#         print(111, self.perimeter)
#         return self.perimeter
#     def set_perimeter(self, new_p):
#         self.perimeter = new_p
#         self.get_perimeter()
# f = Figure(123)
# x = f.get_perimeter()
# f.set_perimeter(222)

# class Student:
#     def __init__(self, name):
#         print('Inside Constructor')
#         self.name = name
#         print('Done')
#     def show(self):
#         print('hello', self.name)
#     def __del__(self):
#         print('Inside Constructor')
#         print('deleted')
#
# s1 = Student('Anna')
# s1.show()
# del s1
# s1.show()

# class Student:
#     '''Документация'''
#     group = []
#     def __init__(self, name):
#         print('Inside Constructor')
#         self.name = name
#         Student.group.append(self.name)
#         print('Done')
#     def show(self):
#         print('hello', self.name)
#     def __del__(self):
#         print(self.name)
#
# s5 = Student('Anna')
# s5.show()
# print(type(s5))
# print(s5.__class__)
# print(isinstance(s5, Student))
# print(dir(s5))
# print(s5.__doc__)

# <class '__main__.Student'>
# <class '__main__.Student'>
# True
# ['__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__'

# x = [1,2,3]
# print(type(x))
# print(isinstance(x, list))
# print(dir(x))

# x = 1
# y = 1.5
# print(isinstance(x, (int, float)))
# print(dir(x))

# Наследование

# class Tree:
#     def __init__(self, kind, height):
#         self.kind = kind
#         self.age = 0
#         self.height = height
#     def grow(self):
#         self.age += 1
# class FruitTree(Tree):
#     def __init__(self, kind, height):
#         super().__init__(kind, height)
#     def give_fruits(self, harvest):
#         print(f'{harvest} kg of {self.kind}')
# f_tree = FruitTree('apple', 0.7)
# # f_tree.give_fruits()
# # f_tree.grow()
# # print(f_tree.age)
# o_tree = FruitTree('orange', 1)
# # o_tree.give_fruits()
# o_tree.give_fruits(30)

# class Figure:
#     def __init__(self, perimeter, color='black'): #сначала позиционный, потом именованный аргумент
#         self.color = color
#         self.perimeter = perimeter
#     def get_perimeter(self):
#         print(self.perimeter)
#         return self.perimeter
#     def set_perimeter(self, new_p):
#         self.perimeter = new_p
#         self.get_perimeter()
# # f = Figure(123)
# # x = f.get_perimeter()
# # f.set_perimeter(222)
# class Triangle(Figure):
#     def __init__(self, a, b, c, color = 'black'):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.color = color
#         self.perimeter = self.set_perimeter()
#     def show(self):
#         print(111, self.a, self.b, self.c, self.perimeter)
#     def set_perimeter(self):
#         self.perimeter = self.a + self.b + self.c
#         self.show()
#         return self.perimeter
# t = Triangle(5,5,5)
# t.show()
# t.set_perimeter()

# class Rectangle(Figure):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.perimeter = self.set_perimeter()
#     def set_perimeter(self):
#         return 2 * (self.a + self.b)
#     def show(self):
#         print(self.a, self.b, self.perimeter)
#
# r = Rectangle(2,3)
# r.show()

#ленивый путин

# class Person1:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 1
#     def display(self):
#         print(f'{self.name}: {self.__age}')
# tom = Person1('Tom')
# tom.__age = 50
# tom.sex = 'M'
# print(tom.display())
# print(tom.sex)
# # dooble underscore - дандер (d+under) - двойное подчеркивание __
# # self.__age = 1 __ - не меняет объект (защищен __)
# print(tom._Person1__age)
# print(tom.__age)

class Data:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, i):
        return self.info[i]
class Teacher:
    def __init__(self):
        self.work = 0
    def teach(self, info, *pupil):
        for i in pupil:
            i.take(info)
            self.work += 1
class Pupil:
    def __init__(self):
        self.knowledge = []
    def take(self, info):
        self.knowledge.append(info)
lesson = Data('class', 'object', 'inheritance')
marvanna = Teacher()
vasy = Pupil()
pety = Pupil()
marvanna.teach(lesson[2], vasy, pety)
marvanna.teach(lesson[0], pety)
print(vasy.knowledge)
print(pety.knowledge)
print(marvanna.work)

дз - при ините учителю пустой списко учеников аппендом добавлять селф
учитель бегает по списку и посылает одну и ту же задачу, потом ученик посылает решение





