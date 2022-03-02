# counting digits in number.
num = int(input("Enter your number"))
digitcnt = 0
while num>0:
    digitcnt += 1
    num = num//10
print("The numbers of digits", digitcnt)


#reverse of a numbers.
n2 = int(input("enter your number "))
rev = 0
while num >0:
    digit = num%10
    rev = rev * 10 + digit
    num = num//10
print("Reverse of your number", rev)
