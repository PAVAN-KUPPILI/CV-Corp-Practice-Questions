x=abs(int(input()))
if x==0:
    print("Invalid Input")
elif x not in range(1,7):
    print("Range Exceeded")
else:
    c=65
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(chr(c),end=" ")
            c+=1
        print()