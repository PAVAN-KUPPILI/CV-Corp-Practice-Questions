n=abs(int(input()))
if n==0:
    print("Invalid Input")
else:
    s=0
    l=[]
    while n!=0:
        l.append(n**2)
        s+=n**2
        n-=1
    print(" + ".join(map(str,l)),f"= {s}")