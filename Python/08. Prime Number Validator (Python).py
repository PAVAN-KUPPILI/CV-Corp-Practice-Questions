x=int(input())
if x<=0:
    print("Invalid Input")
else:
    fc=0
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            fc+=1
            break
    if fc==0:
        print("Prime Number")
    else:
        print("Not a Prime Number")