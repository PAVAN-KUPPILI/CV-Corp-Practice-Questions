x,y=int(input()),int(input())
if x<0 or y<0:
    print("Invalid Inputs")
a=min(x,y)
b=max(x,y)
else:
    f=0
    s=1
    c=0
    while f<=b:
        if f>=a:
            print(f,end=" ")
        f,s=s,f+s
    if c==0:
            c+=1
        print("No Fibonacci Series Values")