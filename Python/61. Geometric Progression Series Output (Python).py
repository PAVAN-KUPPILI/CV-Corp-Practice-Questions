s=int(input())
r=int(input())
n=int(input())
if n<=0:
    print("Invalid Input.")
else:
    l=[]
    for i in range(n):
        gp= s*(r**i)
        l.append(gp)
    s=", ".join(map(str,l))
    print(f"{s}.")