x=int(input())
if x<=0:
    print('Invalid Input.')
else:
    t=x
    l=[]
    while t>0:
        l.append(t%10)
        t//=10
    
    lo=min(l)
    h=max(l)
    span=h-lo
    print(f"Lowest Digit in a Given Number is {lo}.")
    print(f"Highest Digit in a Given Number is {h}.")
    print(f"Highest Span in a Given Number is {span}.")