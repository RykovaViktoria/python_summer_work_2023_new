# class Person:
#     def __init__(self, f, i, o):
#         self.f = f
#         self.i = i
#         self.o = o
#     def __str__(self):
#         return f'{self.o[::-1]}{self.i[::-1]}{self.f[::-1]}'
#
# person = Person('Иванов', 'Михаил', 'Федорович')
# print(person)

class Person:
    def __init__(self, *args):
        self.args = args
    def __str__(self):
        return ''.join(self.args)[::-1]
p = Person('ad','asd','asd')
print(p)
