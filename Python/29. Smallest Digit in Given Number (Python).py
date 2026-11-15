x=int(input())
if x<=0:
    print("Invalid Input.")
else:
    t=x
    l=[]
    while t>0:
        l.append(t%10)
        t//=10
    
    print(f"Smallest Digit in a Given Number is {min(l)}.")