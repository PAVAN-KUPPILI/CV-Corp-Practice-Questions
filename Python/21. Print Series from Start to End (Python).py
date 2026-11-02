x,y=int(input()),int(input())
if x<=0 or y<=0:
    print("Invalid Inputs")
else:
    while x<=y:
    l=[]
        l.append(x)
        x+=100
    print(*l,sep=", ")