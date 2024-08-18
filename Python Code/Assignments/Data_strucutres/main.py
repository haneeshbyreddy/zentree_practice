from DataStructures import Fiboncci, Palindrome, Matrix, Stack

fib = Fiboncci()
print(fib.fiboncci(10))
print(fib.fiboncci_dynamic(10))

pal = Palindrome()
print(pal.is_palindrome('abcdcba'))
print(pal.is_palindrome(1010101))

mat = Matrix()
print(mat.transpose([[3,7],[9,5]]))
print(mat.matrixMult([[1,2],[3,4]], [[5,6],[7,8]]))

sta = Stack()
for i in [1,6,8,9]:
    sta.insert_item(i)
sta.pop_item()
print(sta.len_stack())
print(sta.top_item())
