'''
NAME = input("Enter your Name: ")
for char in NAME:
    if char in "AEIOUaeiou":
        print(char)
print("\n")

# WAP to accept a string and print all the consoment of it.
Name = input("enter your name: ")
for char in Name:
    if (char>="A" and char<="Z") or (char<="a" or char>="z"):
        if char not in "AEIOUaeiou":
            print(char)
'''
#
a_list=[]
for num in range(1,10):
    a_list.append(num)
print(a_list)
