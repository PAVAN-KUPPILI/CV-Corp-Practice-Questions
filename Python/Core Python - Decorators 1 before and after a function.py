def syntax(fun):
    def inner():
        print("Before function execution")
        fun()
        print("After function execution")
    return inner
@syntax
def demo():
    print("Hello Student")
demo()