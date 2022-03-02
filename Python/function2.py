'''
def saywelcome(name,age):
    print("Hi I am", name, "and My age is", age)

#without keyword.
saywelcome("Raj",25)
saywelcome(25,"Jay") # input must be in correct order.

#with keyword.
saywelcome(name="Rohit",age=24)
saywelcome(age=24,name="Ravi")
'''
'''
def sayhi():
    #print("Hii...")
    return'Hii Everyone! '
print(sayhi())
msg=sayhi()
print(msg)
'''
def saywelcome(name,age):
    return f'Hi {name} and my age is {age}'
msg=saywelcome("Jay",25)
print(msg)

def addition(n1,n2):
    return n1+n2
sum=addition(5.6,6)
print(sum)

#Multiple value return
def calc(n1,n2):
    a = n1+n2
    b = n2-n1
    return a,b

ans = calc(7,12)
print('Addition and Substraction is ', ans) #return in a tuple format.


               
