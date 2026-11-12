def wrap():
        user_i=input()
        if user_i.lower()=="yes":
            mbl=input()
            if mbl==phone_number:
                print("Login Successful")
                fun()
            else:
                print("error")
        else:
            print("error")
def validate_decorator(fun):
phone_number = "9876543210"
    return wrap