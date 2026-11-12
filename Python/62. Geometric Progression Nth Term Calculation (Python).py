s=int(input())
r=int(input())
n=int(input())
if n<=0:
    print("InValid Input.")
else:
    print(f"Last term value is : {s*(r**(n-1))}.")