a,b=int(input()),int(input())
x=min(a,b)
y=max(a,b)
if x<0 or y<0:
    print("Invalid Inputs")
else:
    f=0
    s=1
    sm=0
    cnt=0
    while f<=y:
        if f>=x:
            sm+=f
            cnt+=1
        c=f+s
        f=s
        s=c
    if cnt==0:
        print("No Fibonacci Series Values")
    else:
        print(f"{sm/cnt:.2f}")