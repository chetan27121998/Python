# IMPORTIG THE MODELS
from models import Food
import views as vw

menu = '''
1. Add food
2. Delete food.
3. Update food.
4. Show food list.
5. Show food by the ID.
6. Show food by its name.
7. Show food by its type.
8. Sort food list by its name.
9. Sort food list by its price.
10. Exit
'''

choice = -1
while choice != 0:
    print("-"*5,"Welcome to the Gorcery store","-"*5)
    choice = int(input(menu))
    if choice == 1:
        print("Enter the new food: ")
        f_id = int(input("Enter the ID of the food: "))
        f_name = input("Enter the name of the food: ")
        f_type = input("Enter the type of food Veg, Non-Veg, or Dairy food: ")
        f_price = float(input("Enter the price of the food: "))
        food_obj = Food(f_id, f_name,f_type,f_price)
        flag = vw.create(food_obj)
        if flag:
            print("Food is added to the list")
        else:
            print("Food is not added to the list")

    elif choice == 2:
        del_id = int(input("Enter the ID of the food to remove from the list: "))
        f_list = vw.delete(del_id)
        print("Food has been reomved from the list",del_id)

    elif choice == 3:
        print("Enter the Id, Name, Type and Price to update the food list: ")
        f_id = int(input("Enter the ID of the food : "))
        f_name = input("Enter the updated food Name : ")
        f_type = input("Enter the type of the food : ")
        f_price = float(input("Enter the updated price of the food: "))

        new_obj = Food(f_id,f_name,f_type,f_price)
        flag = vw.update(f_id,new_obj)
        if flag:
            print("Food is successfully updated.")
        else:
            print("Food is not update successfully ")

    elif choice == 4:
        f_list = vw.all()
        for food_obj in f_list:
            print(food_obj)

    elif choice == 5:
        f_get_list = int(input("Enter the food ID: "))
        f_list = vw.show_id(f_get_list)
        print(f_list)

    elif choice == 6:
        f_get_list = input("Enter the food Name: ")
        f_list = vw.show_name(f_get_list)
        print(f_list)

    elif choice == 7:
        f_type = input("Enter the type of food Veg, Non-Veg, or Dairy food: ")
        f_list = vw.show_type(f_type)
        print(f_list)

    elif choice == 8:
        f_list = vw.sort_name()
        print(f_list)

    elif choice == 9:
        f_list = vw.sort_price()
        print(f_list)
