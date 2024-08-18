class Stack:
    def __init__(self):
        self.mystack = []
    def insert_item(self, var):
        self.mystack.append(var)
    def top_item(self):
        return self.mystack[self.len_stack()-1]
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
        len = 0
        flag = True
        while flag:
            try:
                self.mystack[len]
            except:
                flag = False
                break
            len += 1
        return len