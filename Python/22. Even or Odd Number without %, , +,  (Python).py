x=int(input())
if x<=0:
    print("Invalid input")
else:
    while x>0:
        x-=2
    print("Even" if x==0 else "Odd")