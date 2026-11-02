x=int(input())
if x==0:
    print("InvaLid Input.")
elif x<0:
    print("Sorry! you have Entered Negative Values.")
else:
    print(f"Sum of 'N' Natural Numbers is {int((x*(x+1))/2)}.")