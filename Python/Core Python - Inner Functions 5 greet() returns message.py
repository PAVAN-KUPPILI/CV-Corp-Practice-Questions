def greet():
    def message():
        print("msg")
    return message
result=greet()
result()