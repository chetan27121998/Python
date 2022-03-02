# WAP to accept number from the numbers and print addition, multiplication ,substraction.
print("1. Addition.");
print("2. Susbtraction");
print("3. Multiplication");
print("4. Division");
print("5. Exit")


choice = int(input("Enter your choice numbers: "));
if (choice>=1 and choice<=4):
    print("Enter two numbers: ");
    num1 = int(input( ));
    num2 = int(input( ));
    if choice == 1:
        res = num1 + num2;
        print("Addition of two numbers = ", res);
    elif choice == 2:
        res = num1 - num2;
        print("Substraction of two numbers = ", res);
    elif choice == 3:
        res = num1 * num2;
        print("Multiplication of two numbers = ",res);
    else:
        res = num1 / num2;
        print("Division of two numbers = ", res);
elif choice == 5:
    exit();
else:
    print("Wrong input...!!!")
