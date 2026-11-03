x=int(input())
if x<=0:
    print("Invalid Input")
else:
    for i in range(1,x+1):
        if x%i==0:
            print(i,end=" ")