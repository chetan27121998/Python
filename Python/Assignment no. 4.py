#01.)Write a program to Accept marks 0f 5 subject each subject out 100 and Display Each subject marks, Total Marks, Percentage and  Grade as per following cirteria.

# Percentage range                Grade

# 100 to 80                        A+

# 80 to 70                         A

# 70 to 60                         B

# 60 to 50                         C

# 50 to 40                         D

# below 40                        Fai

Hin= int(input("Enter subject marks for Hindi: "))
Eng = int(input("Enter subject marks for English: "))
Math = int(input("Enter subject marks for Math: "))
Phys = int(input("Enter subject marks for Physics: "))
Chem = int(input("Enter subject marks for Chemistry: "))

Total = Hin + Eng + Math + Phys + Chem

per = Total / 5

if per>=80 and per<=100:
    grade="A+"
elif per>=70 and per<=80:
    grade="A"
elif per>=60 and per<=70:
    grade="B"
elif per>=50 and per<=60:
    grade="C"
elif per>=40 and per<=50:
    grade="D"
else:
    grade="Fail"

print("Total Number of marks obtain by student is: ", Total)
print("Percentage obtain by student is: ", per)
print("Grade: ",grade)
print()

#02.) Write a Program to Calculate the Simple Interest for Bank Customer for Fixed Deposit

#      a. If customer is Female and Senior Citizen 8% rate

#      b. If customer is Female and Non-Senior Citizen 6% rate

#      c. If customer is Male and Senior Citizen 7% rate

#      d. If customer is Male and Non-Senior Citizen 5% rate
