print("Invalid Inputs")
else:
    a,b=min(x,y),max(x,y)
    l=[]
    for i in range(a,b+1):
        if i%2==1:
            t=i
            c=0
            while t>0:
                c+=1
                t//=10
            t=i
            arm=0
            while t>0:
                arm+= (t%10)**c
                t//=10
            if i==arm:
                l.append(i)
    if len(l)==0:
        print("No Odd Armstrong Numbers.")
    else:
        s=", ".join(map(str,l))
        print(f"Odd Armstrong Numbers in the Given Range is {s}.")