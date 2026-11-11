n=int(input())
if n<0:
    print("INvalid INput")
else:
    for i in range(0,n+1):
        fc=1
        for j in range(1,i+1):
    l=[]
            fc*=j
        l.append(fc)
    st="+".join(map(str,l))
    print(f"{st}={sum(l)}")