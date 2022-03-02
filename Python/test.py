'''
str = 'Hello World!'
print(str[0])
print()

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
print(list[2])
print()

print(22 % 3)
print()

print('hello', 'how', 'are', 'you')
print('hello', 'how', 'are', 'you' + '-' * 4)
print('hello-' + 'how-are-you')
print('hello' + '-' + 'how' + '-' + 'are' + 'you')
print()
'''
str = 'Hello World!'
print(str*2)
print()

n = 10
a=0
b=1
s=0
print("Fibonacci Series:- ",end=" ")
while s<=10:
    print(s,end=" ")
    a=b
    b=s
    s=a+b
print()

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 10:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
