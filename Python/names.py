name = input("Enter your name: ")
age = int(input(" Enter your age: "))

#Hey Chetan! you are 22 years old!

print("Displaying contentin way 1 ")
#End is o parameter that allows to change the output as per your need.
#By default end has \n. \n is escape character meaning new line 
print("Hey ", end="")
print(name, end="!")
print("You are ", end="")
print(age, end="")
print("Years old!")


#Displaying content in Way 2

print("Dipslaying ocntent in Way 2")
print("Hey", name, "! you are", age, "years old!")
