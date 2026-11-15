x=int(input())
if x<=0:
    print("Invalid Input")
else:
    for i in range(x):
        for j in range(1,x+1):
            print(j,end=" ")
        print()