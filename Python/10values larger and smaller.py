#01.) Write the program to accept the 10 values from the user and find the largest and the smallest among them?
NumList = []
print("Please enter the Number of List: ")
for i in range(1, 11):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)
print(NumList)

print("The Smallest Element in this List is : ", min(NumList))
print("The Largest Element in this List is : ", max(NumList))
