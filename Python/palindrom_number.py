n1 = int(input("enter your number: "))
temp = n1
rev = 0
while n1>0:
    digit = n1%10
    rev = rev*10 + digit
    n1 = n1 //10
if temp==rev:
    print("The number is palindrom")
else:
    print("The number is not palindrom")
