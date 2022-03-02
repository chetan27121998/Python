choice = 0
Mylist = []
Selection_Menu = '''1. Add n Value in list.
2. Remove the element by index.
3. Remove the element by values.
4. Count occurance of each value of list.
5. Print sum of all value the list without using built in function.
6. Print min value of list without using built in function.
7. Print max value of list without using built in function.
8. Create a list from unique value of original list.
9. Create a list of even value of orignial list using list comprehension.
10.Create the list with nth of each element from mylist using list comprehension.
'''
while choice != 11:
    print(Selection_Menu)
    choice = int(input("Select your choice "))

    # Add n Value in list.
    if choice == 1:
        n = int(input("How many values you want to add in the list? "))
        for i in range(1,n+1):
            value = int(input(f'enter value-{i}= '))
            Mylist.append(value)
        else:
            print("---List values---")
            print(Mylist)
            print("-"*30)
            
    # Remove the element by index.
    elif choice == 2:
        index = int(input("Enter a index to remove value: "))
        if index >=0 and index <len(Mylist):
            Mylist.pop(index)
            print("---List values---")
            print(Mylist)
            print("-"*30)
        else:
            print("Invlaid Index of Mylist")
            
    # Remove the element by values.
    elif choice == 3:
        value = int(input("Enter a values to remove from the list: "))
        if Mylist.count(value) > 0:
            Mylist.remove(value)
            print("---List values---")
            print(Mylist)
            print("-"*30)
        else:
            print("Value is not found")
            
    # Count occurance of each value of list.
    elif choice == 4:
        x = int(input("Enter your Number which is in the Mylist:"))
        count = 0
        for i in Mylist:
            if i == x:
                print(x, " has occured ",count, "time in list")
                count += 1
            else:
                print("Value not found in list")
        print("-"*30)
        
    # Print sum of all value the list without using built in function.
    elif choice == 5:
        Sum_list = 0
        for i in Mylist:
            Sum_list = Sum_list + i
        print("Sum all values all the values in list are: ", Sum_list)
        print("-"*30)
        
    # Print min value of list without using built in function.
    elif choice == 6:
        Min_list = Mylist[0]
        for i in range(1,len(Mylist)):
            if Min_list > Mylist[i]:
                Min_list = Mylist[i]
        print("Minimun value of the list", Min_list)
        print("-"*30)
        
    #  Print max value of list without using built in function.
    elif choice == 7:
        Max_list = Mylist[0]
        for i in range(1,len(Mylist)):
            if Max_list < Mylist[i]:
                Max_list = Mylist[i]
        print("Maximum value of the list", Max_list)
        print("-"*30)
        
    # Create a list from unique value of original list.
    elif choice == 8:
        Unique_list = []
        for i in Mylist:
            if i not in Unique_list:
                Unique_list.append(i)
        print("Unqiue values from the list:", Unique_list)
        print("-"*30)
        
    # Create a list of even value of orignial list using list comprehension.
    elif choice == 9:
        Even_list = [x for x in Mylist if (x%2)==0] # List Comprehension method used.
        print("Even values in Mylist", Even_list)
        print("-"*30)
        
    # Create the list with nth of each element from mylist using list comprehension.  
    elif choice == 10:
        power = int(input("Enter power ta create list: "))
        powerlist = [i ** power for i in Mylist]   # List Comprehension Methods used.
        print(powerlist)
        print("---List values---")
        print(Mylist)
        print("-"*30)
    # if the user the choice of 11, then program will shows this message and also stop the program at this moment.
    elif choice == 11:
        print("Thank you ....")
        
    # If the user enter the value greater than the 11 , then the program will show this message to user.
    else:
        print("INVALID CHOICE.....")
        
