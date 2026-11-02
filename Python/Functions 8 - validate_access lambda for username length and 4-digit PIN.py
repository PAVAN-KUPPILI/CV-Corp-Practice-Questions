# Write your code here
validate_access= lambda username,pin: username>=6 and len(str(pin))==4
print(validate_access(1234,7))
print(validate_access(7,1234))