a,b,c=int(input()),int(input()),int(input())
if a>0 and b>0 and c>0:
    h=max(a,b)
    h=max(h,c)
    k=h
    while True:
        if h%a==0 and h%b==0 and h%c==0:
            print(h)
            break
        h+=k
elif a<=0 and b>0 and c>0:
    print("InvalId First Input")
elif a>0 and b<=0 and c>0:
    print("Invalid Second Input")
elif a>0 and b>0 and c<=0:
    print("InvaliD ThirD Input")
else:
    print("Sorry Invalid Inputs!")