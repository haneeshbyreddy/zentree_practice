def repeat(n):
    def my_decorator(func):
        def wrapper_1():
            for _ in range(n):
                print("before")
                func()
                print("after")
        return wrapper_1
    return my_decorator

@repeat(2)
def say_hello():
    print("Hello!")

say_hello()