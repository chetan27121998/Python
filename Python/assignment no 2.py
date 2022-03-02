#01. Declare a variable num = 10, use short hand operator to increment num by 10, subtract by 5, divide by 3 and multiply by 4.
num = 10
print("Before increment of number: ",num)
#increment number by 10
num += 10
print("After increment of number by 10: ",num)
#Substract by 5:
num -= 5
print("After substracting by 5: ",num)
#Divide by 3:
num //= 3
print("After dividing by 3: ",num)
#multiply with 4:
num *= 4
print("After multiplying by 4: ",num)
print()

#02. Calculate area and perimeter of an equilateral triangle.
side = float(input("Please Enter length of any side of an Equilateral Triangle: "))
#Area of an Equilateral Triangle:
Area = (side * side) * 1.732/4
print("Area of an Equilateral Triangle is : ",Area)
#Perimeter of an Equilateral Triangle:
Perimeter = 3 * side
print("Perimeter of an Equilateral Triangle is: ",Perimeter)
print()

#03. Declare a student's score in 5 subjects like math, physics, history, english and chemistry. calculate total score and percentage.

#All the Subjects marks entery:
Math = int(input("Enter subject marks for Math : "))
Physics = int(input("Enter subejct marks for Physics : "))
History = int(input("Enter subject marks for History : "))
English = int(input("Enter subejct marks for English : "))
Chemistry = int(input("Enter subject marks for Chemistry : "))
#Total of all the subejcts:
Total = Math + Physics + History + English + Chemistry
print("Total of all the subject is : ", Total)
#Percentage calculation:
Percentage = (Total/500)*100
print("Percentage calculation is : ", Percentage)
print()

#05.If i = 3, j = 2 what is the result of following expressions?
   #1.) i + 5 >= j - 6. 
   #2.)j * 10 < i ** 2.
   #3.)i < j + 5 > j ** 4.
i = 3
j = 2
if i + 5 >= j - 6:
    print("Above Condition is True")
else:
    print("Above Condition is False")
if j * 10 < i ** 2:
    print("Above Condition is True")
else:
    print("Above Condition id False")
if i < j + 5 > j ** 4:
    print("Above Condition is True")
else:
    print("Above Condition is False")
