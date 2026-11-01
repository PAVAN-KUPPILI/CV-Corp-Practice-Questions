x,y=int(input()),int(input())
step= -1 if x>y else 1
for i in range(x,y+step,step):
l=[]
    l.append(f"{i}@{i+step}")
print(*l,sep=",")