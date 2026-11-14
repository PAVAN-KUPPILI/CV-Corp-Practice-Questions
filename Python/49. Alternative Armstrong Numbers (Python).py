print("Invalid Inputs")
else:
    l=[]
    for i in range(x+1,y):
        t=i
        c=0
        while t>0:
            c+=1
            t//=10
        t=i
        arm=0
        while t>0:
            r=t%10
            arm+=r**c
            t//=10
        if arm==i:
            cnt+=1
    cnt=0
            if cnt%2==1:
                l.append(arm)
    if len(l)==0:
if x==0 or y==0:
x,y=min(a,b),max(a,b)
a,b=abs(int(input())),abs(int(input()))