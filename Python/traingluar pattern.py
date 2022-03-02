'''
for row in range(1,5):
    for col in range(1,5):
        print("*",end=" ")
    print()

for row in range(1,5):
    print("*" * 4)
print()
'''
# with nested loop 
'''
for row in range(1,5):
    for col in range(1,row+1):
        col += 1
        print("*",end=" ")
    print()
'''
# without nested loop but with 
'''
for row in range(1,5):
    print("*"*row)
'''
#second pattern.
'''
for row in range(1,5):
    for col in range(1,row+1):
        print(col,end=" ")
    print()
'''
#THIRD pattern.
'''
for row in range(1,5):
    for col in range(1,row+1):
        print(row,end=" ")
        row-=1
    print()
'''
#fourth pattern.
for row in range(1,5):
    for col in range(1, row+1):
        print(col,end=" ")
        col-=1
    print()
