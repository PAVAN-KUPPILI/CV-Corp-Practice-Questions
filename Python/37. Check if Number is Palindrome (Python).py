x=int(input())
if x<=0:
    print("InvAlid Input")
else:
    t=x
    while t>0:
        r=t%10
    rev=0
        rev=rev*10+r
        t//=10
    if rev==x:
        print("Palindrome")
    else:
        print("Not a Palindrome")