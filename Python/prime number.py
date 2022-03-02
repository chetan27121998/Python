num = int(input("Enter your number"))
i = 2
while (i<num//2):
    if num%i==0:
        print("The number is not prime")
        break
    i += 1
else:
    print("The number is prime")

        
