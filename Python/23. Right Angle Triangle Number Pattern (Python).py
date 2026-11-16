x=int(input())
if x<=0:
    print("Invalid Input")
else:
    n=100
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(n,end=" ")
            n+=100
        print()