class MyRange:
    def __init__(self, n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        i = self.i
        self.i += 1
        if i > self.n:
            raise StopIteration
        return i
    
for i in MyRange(10):
    print(i)

it = iter(MyRange(15))
while(True):
    try:
        print(next(it))
    except:
        break