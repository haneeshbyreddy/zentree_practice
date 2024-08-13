add = lambda x, y : x+y
print("add with lamda :",add(1,5))

numbers = [1,2,4,5,7]
squared = list(map(lambda x : x**2, numbers))
print("squared arr with lamda & map :", squared)

numbers = [1,2,3,4,6,7,8]
evens = list(filter(lambda x : x%2 == 0, numbers))
print("even numbers with lamda & filter :", evens)

numbers = [(2, 3), (1, 2), (4, 1), (3, 5)]
sorted_arr = sorted(numbers, key=lambda x : x[0])
print("sorted pairs based on first value :", sorted_arr)

operations = {
    "add": lambda x, y : x+y,
    "sub": lambda x, y : x-y,
}
print("operations with dict and lamda :", )
print("\tadd(1,3) :", operations['add'](1,3))
print("\tsub(1,3) :", operations['sub'](1,3))

