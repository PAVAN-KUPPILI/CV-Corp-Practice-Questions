def login_required(fun):
    def wrapper():
    return wrapper
@login_required
def profile():
        logged_in=True
        if logged_in:
            fun()
        else:
            print("Please login first")
            print("Access granted")
    print("Welcome to profile")
profile()