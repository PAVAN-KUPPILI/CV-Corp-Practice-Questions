x=abs(int(input()))
if x==0:
    print("Invalid Input.")
else:
    while x>=1:
    l=[]
        l.append(x**3)
        x-=1
    
    print(*l,sep=", ",end=".")