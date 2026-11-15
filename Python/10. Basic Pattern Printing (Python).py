if x<=0 or y<=0:
    print("Invalid Inputs")
else:
    for i in range(1,x+1):
        for j in range(1,y+1):
            if j==1 or j==y or i==1 or i==x:
                print("*",end=" ")
            else:
                print("$",end=" ")
        print()