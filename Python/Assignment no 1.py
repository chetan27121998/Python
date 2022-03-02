#01. Write a program to accept a name from user and print it.
Name = input("Enter your name: ")
if Name=="Chetan":
    print(Name)
else:
    print("Invalid Name")
print()

#02. Write a program to accept 3 number and print its multiplication.
n1 = int(input("Enter your first number: ")) #type of n1 is integer.
n2 = int(input("Enter your second number: ")) # type of n2 is integer.
n3 = int(input("Enter your third number: ")) # type of n3 is integer.
MULTI = n1 * n2 * n3  # PROCESS
print(n1,"*",n2,"*",n3,"=",MULTI)
print()

#03. Write a program to accept 2 number and swap them with using 3rd variable.
num1 = int(input("Enter your first number")) #type of num1 is integer.
num2 = int(input("Enter your second number")) #type of num2 is integer.
print("before swaping number: ",num1,num2)
temp = num1
num1 = num2
num2 = temp
print("after swaping number: ",num1,num2)
print()

#04.Write a program to accept 2 number and swap them without using 3rd variable.
num3 = int(input("Enter your first number: "))
num4 = int(input("enter your seconsd number: "))
print("before swaping number: ",num3,num4)
num3 = num3 + num4
num4 = num3 - num4
num3 = num3 - num4
print("after swaping number: ",num3,num4)
