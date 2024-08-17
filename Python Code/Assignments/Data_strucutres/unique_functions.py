from functools import reduce

squares = [x**2 for x in range(10)]

for index, value in enumerate(['a', 'b', 'c']):
    print(f"index: {index}, value: {value}")

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

squares_dict = {x: x**2 for x in range(5)}

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world!"