r,c=int(input()),int(input())
if r<=0 and c<=0:
    print("Invalid Row and Column Values")
elif r<=0 and c>0:
    print("Invalid Row Value")
elif r>0 and c<=0:
    print("Invalid Column Value")
else:
    for i in range(1,r+1):
        for j in range(1,c+1):
    s=1
            print(f"{s}*" if j!=c else s,end="")
            s+=1