a=int(input())
d=int(input())
n=int(input())
if n<=0:
    print("Invalid Input.")
else:
    sm=0
    for i in range(n):
        ap= a+(d*i)
        gp=1/ap
        sm+=gp
    print(f"{sm:.2f}")