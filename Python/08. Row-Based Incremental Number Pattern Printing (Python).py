x=int(input())
if x<=0:
    print("Invalid Input")
else:
    for i in range(1,x+1):
        for j in range(1,x+1):
            print(i if i+j>=x+1 else 1,end=" ")
        print()