x,y=int(input()),int(input())
if x<=0 or y<=0:
    print("Invalid Inputs")
else:
    l=[]
    for i in range(x,y+1):
        if i%2==r:
            l.append(f"{i}^2")
    r= 1 if x%2==1 else 0
    print(*l,sep=", ")