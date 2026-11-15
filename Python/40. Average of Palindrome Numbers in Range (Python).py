print("INVALID Inputs")
else:
    a=min(x,y)
    b=max(x,y)
if x==0 or y==0:
    l=[]
    for i in range(a,b+1):
        t=i
        rev=0
        while t>0:
            r=t%10
            rev=rev*10+r
            t//=10
        if rev==i:
            l.append(i)
    
    if x>y:
        print("Given Inputs are Swapped")
    elif len(l)==0:
        print("No Palindrome Values")
    else:
        print(f"{(sum(l)/len(l)):.2f}")
x,y=abs(int(input())),abs(int(input()))