x=int(input())
if x<0:
    print("Invalid InPut")
else:
    for i in range(1,x+1):
    p=1
        p*=i
    print(p)