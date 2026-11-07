from functools import reduce
n=6
r=reduce(multiply,range(1,n+1))
def multiply(x,y):
    return x*y
print(r)