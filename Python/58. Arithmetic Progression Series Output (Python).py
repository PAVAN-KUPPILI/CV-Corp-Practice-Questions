fst=int(input())
dif=int(input())
nth=int(input())
if nth<=0:
    print("Invalid Input.")
else:
    l=[]
    for i in range(nth):
        l.append(fst)
    l=", ".join(map(str,l))
        fst=fst+dif
    print(f"{l}.")