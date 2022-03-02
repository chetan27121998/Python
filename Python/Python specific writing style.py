# WAP TO CREATE FUNCTION TO RETURN MULTIPLICATION OF 3 NUMBER WITH 1 REQUIRED
# AND 2 DEFAULT
def Multiple(n1,n2=1,n3=1):
    return n1*n2*n3
print("Multiplication is ", Multiple(5))

# Function with varibale number of agrument(vararg's).
def add(*num):
    sum = 0
    for n in num:
        sum += n
    print("Addition is ", sum)

add(3,7,8,9,7,5,7)

# This function working on iterable one.
l1 = [1,2,17,8,9]
additionofl1= sum(l1)
print(additionofl1)
maximum=max(l1)
print(maximum)
minimum=min(l1)
print(minimum)
sortedl2=sorted(l1) # ASCENDING.
print(sortedl2)
print()

l2 = [1,2,3,4,5,6,7,8]
def iseven(n):
    return n%2==0
evenAdd=sum(l1,iseven)
print("Sum of even number of l2 ", evenAdd)
