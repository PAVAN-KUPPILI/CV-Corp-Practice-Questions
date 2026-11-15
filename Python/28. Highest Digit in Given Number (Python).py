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
    print(f"Highest Digit in a Given Number is {max(l)}.")