n=int(input())
if n<=0:
    print("Invalid Input")
else:
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(s,end=" ")
        s=n
            s-=1
        print()