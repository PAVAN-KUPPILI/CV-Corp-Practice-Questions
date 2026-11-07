def fun(*args):
    po=1
    for i in args:
        po*=i
    return po
print(fun(1,2,3))