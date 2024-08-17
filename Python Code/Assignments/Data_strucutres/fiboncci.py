n = 30
print('for n :', n)

# recursion
recursion_count = 0
def fiboncci(n):
    global recursion_count
    recursion_count += 1
    if n == 1 or n == 2:
        return 1
    return fiboncci(n-1) + fiboncci(n-2)

# dynamic recursion
mydict = {1: 1, 2: 1}
dynamic_recursion_count = 0

def fiboncci_dynamic(n):
    global dynamic_recursion_count
    dynamic_recursion_count += 1
    if n in mydict:
        return mydict[n]
    mydict[n] = fiboncci_dynamic(n-1) + fiboncci_dynamic(n-2)
    return mydict[n]
    

# print(fib_arr)
print(fiboncci(n))
print(fiboncci_dynamic(n))
print(recursion_count, dynamic_recursion_count)