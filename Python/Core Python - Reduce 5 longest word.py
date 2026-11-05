from functools import reduce
l=["as","1swd","eeawaew"]
x=reduce(lambda x,y: x if len(x)>len(y) else y,l)
print(x)