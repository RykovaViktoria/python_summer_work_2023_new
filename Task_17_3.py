# class Shape:
#     def __init__(self, color, square):
#         self.color = color
#         self.square = square
#     def set_color(self):
#         self.color = input('Введите цвет объекта -->')
#     def print_color(self):
#         print(f'{self.color}')
#     def set_square(self):
#         self.square = int(input('Введите площадь объекта -->'))
#     def print_square(self):
#         print(f'{self.square}')
#
# a = Shape('',0)
# a.set_color()
# a.print_color()
# a.set_square()
# a.print_square()
#

class Shape:
    def __init__(self, color, square=10):
        self.color = color
        self.square = square
    def get_color(self):
        return self.color
    def set_color(self, new_color):
        self.color = new_color

a = Shape('Red')
a.get_color()