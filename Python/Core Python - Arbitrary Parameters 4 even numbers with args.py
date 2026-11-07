def fun(*args):
    l=list(filter(lambda x:x%2==0,args))
    return l
print(fun(1,2,3,4,5,6,7,8,7,7,2))