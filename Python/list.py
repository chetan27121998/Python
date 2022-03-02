#
list = ["raj","chetan","rahul"]
for name in list:
    print(name)
print("n\n")


# dictionary
d1 = { "EmpID" : 123,
       "EmpName" : "Rahul",
       "EmpSal" : 25000
       }
for EmpDetail in d1:
    print(EmpDetail, "=",d1[EmpDetail])
print(EmpDetail["EmpID"])
