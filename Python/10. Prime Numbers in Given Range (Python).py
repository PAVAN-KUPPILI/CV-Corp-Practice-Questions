x,y=int(input()),int(input())
if x<=0 or y<=0:
    print("Invalid Inputs")
else:
    l=[]
    for i in range(x,y+1):
        for j in range(1,i+1):
        fc=0
            if i%j==0:
                fc+=1
        if fc==2:
            l.append(i)
    print(", ".join(map(str,l)))