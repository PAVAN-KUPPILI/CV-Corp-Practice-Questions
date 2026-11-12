def my_decorator(func):
    def wrapper():
        print("Welcome Message")
    return wrapper
@my_decorator
def greet():
        func()
        print("Thank You Message")
    print("Good Morning")
greet()