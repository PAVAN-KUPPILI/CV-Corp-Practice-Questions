def validate_positive(fun):
    def wrapper(*args):
        if any(arg<0 for arg in args):
            print("ERROR NEGITIVE NUMBER DETECTED")
            return None
        else:
            return fun(*args)
    return wrapper
@validate_positive
def multiply(a,b):
    return a*b
print(multiply(1,2))