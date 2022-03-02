# No parameter with no return.
def add():
    n1 =2
    n2 =4
    print("Addition", n1+n2)
add()
print()
#Parameter with no return.
def substract(n3,n4):
    print("Substraction", n3-n4)
substract(56,49)
print()
#Parameter with return
def multiple(n5,n6):
    return n5*n6
print("Multiplication is ", multiple(5,6))
print("Multiplicatino is ", multiple(11,2))
print()
#No parameter with return.
def  Add():
    n7=7
    n8=5
    return n7+n8
print("Addition is ", Add())
print()
#Python spcific writing style.
# function with default parameter.
def Substract(n1,n2=0):
    return n1-n2
print("Substract is", Substract(3))
print("Substract is", Substract(3,7))
