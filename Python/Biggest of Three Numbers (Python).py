x,y,z=int(input()),int(input()),int(input())
ans= x if (x>y and x>z) else y if (y>z and y>x) else z
print(f"{ans} is a Biggest Number from the Given Numbers")