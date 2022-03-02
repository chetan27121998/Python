'''
for i in range(1,5):             #****
    for j in range(4,i-1,-1):     ***
        print("*",end=" ")        **
    print()                       *


for row in range(1,5):             
    for col in range(4,row-1,-1):   
        print(col,end=" ")          
    print()                         

for row in range(4,0,-1):
    print("*"*row)

for row in range(1,5):                   #    *
    for space in range(4,row-1,-1):          **
        print(" ",end=" ")                  ***
    for col in range(1,row+1):             ****
        print("*",end=" ")
    print()
'''
for row in range(1,5):
    for sp in range(4,row,-1):
        print(" ",end="")
    for star in range(4,row+1):
        print("*",end="")
    print()
