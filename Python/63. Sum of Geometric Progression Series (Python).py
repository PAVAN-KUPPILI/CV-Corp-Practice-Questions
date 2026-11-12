s=int(input())
r=int(input())
n=int(input())
if n<=0:
    print("Invalid Input")
else:
    gm=0
    for i in range(n):
        sm=s*(r**i)
        gm+=sm
    print(gm)