from functools import reduce
x=[1,2,3,4,5,6]
r=reduce(lambda x,y:x+1 if y%2==0 else x,x,0)
print(r)