x=int(input())
if x<=0:
    print("Invalid Input" if x<0 else "Zero")
else:
    t=x
    rev=0
    while t>0:
        r=t%10
        rev = rev*10+r
        t//=10
    if rev==x:
        print("Given Number is Palindrome")
    else:
        print(f"Reverse of a Given Number is {rev}")