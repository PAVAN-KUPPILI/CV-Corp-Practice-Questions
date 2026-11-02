x=int(input())
l=[]
for i in range(1,x+1):
    if i%5==0:
        l.append("divisible by five")
    if i%2==0:
        continue
    else:
        l.append(i)
print(", ".join(map(str,l)))