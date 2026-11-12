s=int(input())
d=int(input())
n=int(input())
if n<=0:
    print("InvaliD InPut")
else:
    ap=s+(n-1)*d
    if ap==0:
        print("InvaliD InPut")
    else:
        hp=1/ap
        print(f"{hp:.2f}")