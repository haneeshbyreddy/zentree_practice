class Helper:
    def __init__(self):
        self.mystack = []
    def insert_item(self, var):
        self.mystack.append(var)
    def pop_item(self):
        var = self.mystack[self.len_stack()-1]
        self.mystack = self.mystack[:self.len_stack() - 1]
        return var
    def is_empty(self):
        try:
            self.mystack[0]
        except:
            return True
        return False
    def len_stack(self):
        return len(self.mystack)
        # len = 0
        # flag = True
        # while flag:
        #     try:
        #         self.mystack[len]
        #     except:
        #         flag = False
        #         break
        #     len += 1
        # return len

stack = Helper()

for i in range(4):
    stack.insert_item(i)
    print("inserted :", i)

print("is stack empty :", stack.is_empty())
print("len of stack ", stack.len_stack())

for i in range(4):
    print("pop ", stack.pop_item())

print("is stack empty :", stack.is_empty())
print("len of stack ", stack.len_stack())
