from functools import reduce
l=[1,2,4,2,1]
x=reduce(lambda x,y:x if x>y else y,l)
print(x)