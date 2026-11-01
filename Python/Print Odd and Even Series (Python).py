x=int(input())
for i in range(1,x+1):
    if i % 2==0:
        l.append("even")
    else:
l=[]
        l.append(i)
print(*l,sep=", ")