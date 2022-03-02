# WAP to print all numbers between 101 to 150 those are divisible by 5.
for i in range(105,151,5):
    print(i, end= " ")
print("\n")

#WAP to print table of numbers enter by user.
num = int(input("Enter your number: "))
for i in range(1,11):
    print(num, "*",i,"=",num*i)
print("\n")

#Second way
n1 = int(input("Enter your numbers: "))
for i in range(n1,n1*10+1,n1):
    print(i, end=" ")

