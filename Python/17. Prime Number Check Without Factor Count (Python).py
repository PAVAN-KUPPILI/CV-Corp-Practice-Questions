x=int(input())
if x<=0:
    print("Invalid Input")
else:
    is_prime=True
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            is_prime=False
    
    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")