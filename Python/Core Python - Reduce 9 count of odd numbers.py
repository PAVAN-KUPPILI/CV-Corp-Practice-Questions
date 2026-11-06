from functools import reduce
l=[1,2,3,4,5,6,5,3]
x=reduce(lambda x,y : x+1 if y%2==1 else x,l,0)
print(x)