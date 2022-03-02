# WAP to accept a string and print all the consoment of it.
Name = input("enter your name: ")
for char in Name:
    if (char>="A" and char<="Z") or (char<="a" or char>="z"):
        if char not in "AEIOUaeiou":
            print(char)
