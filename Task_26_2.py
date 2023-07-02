def dis(self):
    for k,v in self.__dict__.items():
        print(k,v)
Pet = type('Pet', (), {'dis':dis})
my_cat = Pet()
my_cat.name = 'Rokky'
my_cat.age = 2
dis(my_cat)

