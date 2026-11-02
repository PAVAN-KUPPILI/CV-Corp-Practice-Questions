x,y=int(input()),int(input())
step= 1 if x<y else -1
for i in range(x,y+step,step):
l=[]
    if i>=0:
        l.append(i*5)
    else:
        l.append(f"({i*5})")
print(*l,sep=", ")