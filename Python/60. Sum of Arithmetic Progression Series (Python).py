s=int(input())
d=int(input())
n=int(input())
if n<=0:
    print("Invalid input.")
else:
    l=[]
    for i in range(n):
        l.append(s)
        s=s+d
    st=" + ".join(map(str,l))
    print(f"{st} = {sum(l)}.")