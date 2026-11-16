n=abs(int(input()))
if n==0:
    print("Invalid Input")
else:
    c=2
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(c,end=" ")
            c+=2
        c-=1
        print()