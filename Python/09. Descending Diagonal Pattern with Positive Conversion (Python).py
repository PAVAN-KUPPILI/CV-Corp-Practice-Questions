x=abs(int(input()))
if x==0:
    print("InvaliD Input")
else:
    for i in range(x,0,-1):
        for j in range(x,0,-1):
            print(i if i>=j else j,end="")
        print()