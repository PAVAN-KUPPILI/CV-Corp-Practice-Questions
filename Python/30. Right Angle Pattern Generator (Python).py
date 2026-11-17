x,y=int(input()),int(input())
if x<=0 and y%2==0:
    print("Invalid Inputs")
elif x<=0:
    print("Invalid Row Value")
elif y==0 or y%2==0:
    print("Invalid Starting Value")
else:
    for i in range(1,x+1):