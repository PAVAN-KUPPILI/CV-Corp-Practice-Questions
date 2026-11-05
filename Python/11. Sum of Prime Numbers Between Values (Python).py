x,y=int(input()),int(input())
if x<=0 or y<=0:
    print("Invalid Inputs")
else:
    sm=0
    for i in range(x+1,y):
        fc=0
        for j in range(1,i+1):
            if i%j==0:
                fc+=1
        if fc==2:
            sm+=i
    print(sm)