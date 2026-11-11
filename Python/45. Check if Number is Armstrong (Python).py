n=int(input())
if n<=0:
    print("Invalid Input")
else:
    t=n
    cnt=0
    while t>0:
        cnt+=1
        t//=10
    t=n
    temp=0
    while t>0:
        r=t%10
        temp+=r**cnt
        t//=10
    if temp==n:
        print(f"{n} is a Armstrong Number.")
    else:
        print(f"{n} is Not a Armstrong Number.")