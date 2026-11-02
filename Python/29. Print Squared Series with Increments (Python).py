x,y=float(input()),float(input())
l=[]
while round(x,1) <=y:
    l.append(f"{x}^2")
    x= round((x+0.2),1)
print(*l,sep=", ",end=".")