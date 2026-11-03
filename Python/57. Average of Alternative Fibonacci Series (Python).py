x,y=int(input()),int(input())
a=min(x,y)
b=max(x,y)
if a<0 or b<0:
    print("Invalid Inputs")
else:
    f=0
    s=1
    c=1
    l=[]
    while f<=b:
        if f>=a:
            if c%2==0:
                l.append(f)
        t=f+s
        f=s
        s=t
    
    if len(l)==0:
            c+=1
       print("No Fibonacci Series Values")