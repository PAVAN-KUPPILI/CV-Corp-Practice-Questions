if x<=0 or y<=0:
    print("Invalid Inputs")
else:
    sm=c=0
    for i in range(x+1,y):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            c+=1
            if c%2==1:
                sm+=i
    if c==0:
        print("No Prime Numbers")
    else:
        print(sm)
x,y=int(input()),int(input())