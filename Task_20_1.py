import time
import pandas as pd
class Cafe:
    def __init___(self):
        self.name = name
    def order(self):
        menu = [{'Latte': 150, 'Americano': 100, 'Ekler': 80, 'Pancho': 120}]
        df = pd.DataFrame(menu)
        df1 = df.T
        df1.columns = ['Price']
        print(df1)
        dct_order = {}
        menu = {'Latte': 150, 'Americano': 100, 'Ekler': 80, 'Pancho': 120}
        s = list(input('Ваш заказ (введите из меню через пробел) -->').split())
        su = 0
        for i in s:
            print(i, menu[i])
            su += menu[i]
        return f'Total - {su}'

    def client(self, name):
        name = name
        date = time.ctime()
        return f'Info: {name}, {date}'

nump = Cafe()
while True:
    print(nump.order())
    print(nump.client('Tom'))

