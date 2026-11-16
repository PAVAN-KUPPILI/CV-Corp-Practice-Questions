x=int(input())
if x<=0:
    print("Invalid Input")
else:
    for i in range(x,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()