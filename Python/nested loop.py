#WAP to print prime number between 1 to 100.
for num in range(1,101):    # outer loop. which define range of number.
    for i in range(2,num):  # inner loop, which check number is prime or not
        if num%i==0:
            break
    else:
        print(num,end=" ")
print()
