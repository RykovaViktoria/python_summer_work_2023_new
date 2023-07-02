class Person:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age >= 1 and age <=100:
            self.__age = age
        else:
            raise ValueError('Недопустимый возраст')

    @age.deleter
    def age(self):
        del self.__age

Tom = Person(20)
Tom.age = 120