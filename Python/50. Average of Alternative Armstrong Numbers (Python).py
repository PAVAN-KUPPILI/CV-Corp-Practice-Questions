while t>0:
            r=t%10
            arm+=r**c
            t//=10
        if arm==i:
            al+=1
            if al%2==1:
                l.append(i)
    
    if len(l)==0:
        print("No Armstrong Numbers in a Given Range")
    else:
        s=" + ".join(map(str,l))
        print(f"Average of Alternative Armstrong Numbers in the Given Range is ( 
        {s} ) / {len(l)} = {(sum(l)/len(l)):.2f}")