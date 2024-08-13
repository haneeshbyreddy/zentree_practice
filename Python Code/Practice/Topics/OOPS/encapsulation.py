class Base:
    def __init__(self):
        self.a = 1
        self.__a = 1
    def show(self):
        print("a : ",self.a)
        print("__a : ",self.__a)
    

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.a += 1
    def show(self):
        print("a : ",self.a)
        print("__a : ",self.__a)


print("Base class")
obj1 = Base()
obj1.show()

print("Derived class")
obj2 = Derived()
obj2.show()