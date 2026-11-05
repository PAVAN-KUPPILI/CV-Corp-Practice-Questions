from functools import reduce
x=reduce(lambda x,y: x+y**2,l,0)
l=[1,2,3,4,5,6]
print(x)