x=abs(int(input()))
if x==0:
    print("Invalid Input")
else:
    f=0
    s=1
    for i in range(x):
        print(f, end=" ")
        c=f+s
        f=s
        s=c