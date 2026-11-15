x=int(input())
if x==0:
    print("InvaliD Input")
else:
    c=0
    t=abs(x)
    while t>0:
        c+=1
        t//=10
    
    if x>0:
        if c==1:
            print(f"Given Number consists of only 1 Digit.")
        else:
            print(f"Given Number consists of {c} Digits.")
    else:
        if c==1 and x<0:
            print(f"Given Number consists of only 1 Digit and it is Negative Value.")
        else:
            print(f"Given Number consists of {c} Digits and it is Negative Value.")