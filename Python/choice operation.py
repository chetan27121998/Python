# WAP
menu = '''
      1. Sqaure.
      2. Cube.
      3. Exit.
'''
choice = 0
while choice != 3:
    print(menu)
    choice = int(input("enter your choice"))
    if choice>0 and choice<3:
        num = int(input("Enter your Number:- "))

    if choice == 1:
        Sq == num ** 2
        print("Sqaure of",num, "is",Sq)

    elif choice == 2:
        Cu == num ** 3
        print("Cube of",num,"is",Cu)
    elif choice == 3:
        print("Thank you ...")

    else:
        print("Invalid entery")
