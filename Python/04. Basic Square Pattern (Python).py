x=int(input())
if x<=0:
    print("InValid InPut")
else:
    for i in range(1,x+1):
        for j in range(x):
            print(i,end=" ")
        print()