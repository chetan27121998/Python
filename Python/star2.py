'''
for row in range(1,5):
    for col in range(1,5):
        print("*",end=" ")
    print()

for row in range(1,5):
    print("*" * 4)
print()

# instead of star print number using while loop.
row = 1
while row < 5:
    col=1
    while col < 5:
        print(col,end=" ")
        col += 1
    print()
    row += 1
# instead of star print number using while loop.
row = 1
while row < 5:
    col=1
    while col < 5:
        print(row,end=" ")
        col += 1
    print()
    row += 1
print()

# instead of star print number using while loop.
for row in range(1,5):
    for col in range(1,5):
       print(row,end=" ")
       row += 1
    print("-",row)
'''
for row in range(1,5):
    for col in range(1,5):
        print(row+col,end=" ")
    print()
       
