from functools import reduce
l=[1,2,3,4,5]
x=reduce(lambda x,y: x+y,l,0)
print(x)