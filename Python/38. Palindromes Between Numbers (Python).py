x,y=int(input()),int(input())
a,b=min(x,y),max(x,y)
if x<0 or y<0:
    print("InvaliD InputS")
else:
    c=0
    for i in range(a+1,b):
        t=i
        rev=0
        while t>0:
            r=t%10
            rev=rev*10+r
            t//=10
        if i==rev:
            c+=1
            print(i)
    
    if c==0:
        print("No Palindrome Values")