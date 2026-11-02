x=int(input())
if x<=0:
    print("Invalid Input")
else:
    s=c=0
    while x>0:
        r=x%10
        c+=1
        if c%2==1:
            s+=r
        x//=10
    print(s)