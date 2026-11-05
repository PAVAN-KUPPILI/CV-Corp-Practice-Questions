from functools import reduce
l=[1,2,3,4,1,0]
x=reduce(lambda x,y:x if x<y else y,l)
print(x)