x=int(input())
if x<=0:
    print("Invalid Input")
else:
    for i in range(1,x+1):
        for j in range(1,i+1):
            print("@" if i%2==1 else "#",end=" ")
        print()