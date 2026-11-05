def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def calculator(a,b,operation):
    return operation(a,b)
print(calculator(1,2,add))
print(calculator(1,2,subtract))