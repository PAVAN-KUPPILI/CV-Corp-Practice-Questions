n=abs(int(input()))
if n==0:
    print("Invalid Input")
else:
    c=0
    for i in range(2,n+1):
        fc=0
        for j in range(1,i+1):
            if i%j==0 and n%i==0:
                c=c+1
                fc+=1
        if fc==2:
            print(i,end=" ")
    if c==0: