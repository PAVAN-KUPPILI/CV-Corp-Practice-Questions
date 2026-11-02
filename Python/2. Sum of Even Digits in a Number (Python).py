x=int(input())
if x<=0:
    print("Invalid Input")
else:
    s=0
    while x>0:
        r=x%10
        if r%2==0:
            s+=r
        x//=10
    print(s)