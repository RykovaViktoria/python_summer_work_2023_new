class Fib:
    def __init__(self, limit):
        self.first = 1
        self.second = 0
        self.value = 0
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        self.value = self.first + self.second
        self.first = self.second
        self.second = self.value
        if self.value > self.limit:
            raise StopIteration
        return self.value
f = Fib(100)
for i in f:
    print(i)
    input()