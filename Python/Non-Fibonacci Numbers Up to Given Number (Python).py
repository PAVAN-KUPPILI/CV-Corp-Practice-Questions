else:
    f=0
    s=1
    l=[]
    cn=0
    while f<=x:
        l.append(f)
        c=f+s
        f=s
        s=c
    for i in range(x+1):
        if i not in l:
            print(i,end=" ")
            cn+=1
    
    if cn==0:
        print("No Fibonacci Values")
        
    print("Invalid Input")
            