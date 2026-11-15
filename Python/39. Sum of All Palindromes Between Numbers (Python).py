x,y=abs(int(input())),abs(int(input()))
a,b=min(x,y),max(x,y)
if x==0 or y==0:
    print("INVALID Inputs")
else:
    for i in range(a+1,b):
        t=i
        rev=0
        while t>0:
            r=t%10
            rev=rev*10+r
            t//=10
        if rev==i:
    sm=0
            sm+=i
    if sm==0:
        print("No Palindrome Values")
    else:
        print(sm)