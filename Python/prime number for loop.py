# WAP to accept the number from user and check whether it is prime or not using for loop.
num = int(input("Enter your numbers: "))
for i in range(2,num):
    if num%i==0:
        print("it is not prime")
        break
else:
    print("it is prime")
print("\n")

"""
Repeatedly print output 
num = int(input("Enter your numbers: "))
for i in range(2,num):
    if num%i==0:
        print("it is not prime")
        break
else:
    print("it is prime")
"""
#continue
for i in range(1,11):
    if i == 5 or i == 7:
        continue
    print(i)
print("good bye...")
