x=int(input())
if x<=0:
    print("Given Value is Invalid")
else:
    s=1
    for i in range(1,x+1):
        for j in range(1,x+1):
            print("*" if s%4==0 else s,end=" ")
            s+=1
        print()