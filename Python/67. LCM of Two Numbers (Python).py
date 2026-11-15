print("Invalid First Input")
elif a>0 and b<=0:
    print("InValid Second Input")
else:
    H=max(a,b)
    k=H
    while True:
        if H%a==0 and H%b==0:
            print(H)
            break
        H+=k