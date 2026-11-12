attempts=0
def decorator(fun):
    def wrapper():
        global attempts
        attempts+=1
        print(attempts)
        fun()
    return wrapper
@decorator
def start_exam():
    print("Exam Started Successfully")
start_exam()
start_exam()
start_exam()