s=int(input())
r=int(input())
n=int(input())
if n<=0:
    print("Invalid Input")
else:
    l=[]
    for i in range(n):
        hp = f"{1/(s+r*i):.2f}"
        l.append(hp)
    s=", ".join(map(str,l))
    print(s)