x=int(input())
if x<=0:
    print("InValid Input")
else:
    t=x
    while t>0:
    rev=0
        r=t%10
        rev= rev*10+r
        t//=10
    print(rev)