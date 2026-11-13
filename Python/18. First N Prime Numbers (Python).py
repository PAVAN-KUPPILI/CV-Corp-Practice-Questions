n=int(input())
if n<=0:
    print("Invalid Input")
else:
    l=[]
    a=2
    while len(l)<n:
        fc=True
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                fc=False
                break
        if fc:
            l.append(a)
        a+=1
    st=", ".join(map(str,l))
    print(st)