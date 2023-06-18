class Lat:
    def __init__(self, limit):
        self.index = 0
        self.limit = limit
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.liter = chr(ord('A')+self.index)
        self.index += 1
        self.count += 1
        if self.count > self.limit:
            raise StopIteration
        if self.index > 26:
            self.index = 0
            self.liter = chr(ord('A') + self.index)
            self.index += 1
            self.count += 1
        return f'{self.index}, {self.liter},'
l = Lat(50)
for i in l:
    print(i, end = ' ')


