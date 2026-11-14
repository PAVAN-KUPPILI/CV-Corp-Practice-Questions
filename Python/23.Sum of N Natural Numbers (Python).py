n=int(input())
if n==0:
    print("InvaLid Input.")
elif n<0:
    print("Sorry! you have Entered Negative Values.")
else:
    s=0
    l=[]
    for i in range(1,n+1):
        l.append(i)
    s=" + ".join(map(str,l))
    print(f"Sum of 'N' Natural Numbers is {s} = {sum(l)}.")