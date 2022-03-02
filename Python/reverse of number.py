#reverse of a numbers.
n2 = int(input("enter your number "))
rev = 0
while n2>0:
    digit = n2%10
    rev = rev * 10 + digit
    n2 = n2//10
print("Reverse of your number", rev)
