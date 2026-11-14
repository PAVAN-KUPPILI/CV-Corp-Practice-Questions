b=int(input())
if x<=0 or y<=0:
    print("Invalid Inputs")
else:
    l=[]
    for i in range(x,y+1):
        t=i
        c=0
a=int(input())
x,y=min(a,b),max(a,b)
        while t>0:
            c+=1
            t//=10
        t=i
        arm=0
        while t>0:
            r=t%10
            arm+= r**c
            t//=10