x,y,z=int(input()),int(input()),int(input())
    for i in range(l,0,-1):
        if x%i==0 and y%i==0 and z%i==0:
            print(i)
if x>0 and y>0 and z>0:
    l=min(x,y,z)
            break
elif x<=0 and y>0 and z>0:
    print("Invalid First Input")
elif x>0 and y<=0 and z>0:
    print("Invalid Second Input")
elif x>0 and y>0 and z<=0:
    print("Invalid Third Input")
else:
    print("Invalid Inputs")