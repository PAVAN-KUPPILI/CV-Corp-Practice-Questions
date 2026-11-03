x=int(input())
if x<=0:
    print("Invalid Input")
else:
    f,s=0,1
    sm=0
    for i in range(x):
        sm+=f
        f,s=s,f+s
    print(sm)