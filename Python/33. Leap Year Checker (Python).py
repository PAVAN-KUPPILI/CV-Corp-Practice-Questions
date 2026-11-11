yr=int(input())
if yr <= 0:
    print("Given Year is Invalid Input.")
else:
    if yr%400==0 or (yr%4==0 and yr%100!=0):
        print("Leap Year.")
    else:
        print("Not a Leap Year.")