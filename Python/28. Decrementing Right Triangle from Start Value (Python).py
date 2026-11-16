x,y=int(input()),int(input())
if x<=0:
    print("Invalid Input")
else:
    for i in range(x,0,-1):
        for j in range(1,i+1):
            print(y,end=" ")
            y-=1
        print()