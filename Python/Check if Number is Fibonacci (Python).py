else:
    print("Invalid Input.")
if x<0:
x=int(input())
    f=0
    s=1
    while f>=0 and f<x:
        c=f+s
        f=s
        s=c
    if f==x:
        print("Fibonacci Number")
    else:
        print("Not a Fibonacci Number")