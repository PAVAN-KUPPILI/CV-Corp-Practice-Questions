x=int(input())
if x<=0:
    print("Invalid Input.")
else:
    t=x
    l=[]
    while t>0:
        r=t%10
        l.append(r)
        t//=10
    
    s=" + ".join(map(str,l[::-1]))