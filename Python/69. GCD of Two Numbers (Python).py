x,y=int(input()),int(input())
if x<=0 and y<=0:
else: 
    for i in range(l,0,-1):
        if x%i==0 and y%i==0:
    l=min(x,y)
    print("Invalid Inputs")
elif x<=0 and y>0:
    print("Invalid First Input")
elif x>0 and y<=0:
    print("Invalid Second Input.")
            print(i)