x=int(input())
if x<=0:
    print("InvaliD Input")
else:
    if int(x**0.5)*int(x**0.5)==x:
        print("Given Number is a Perfect Square.")
    else:
        print("Given Number is Not a Perfect Square.")