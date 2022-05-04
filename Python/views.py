from models import Food
food_list = []


food_list.append(Food(1,"Apple","Veg",50))
food_list.append(Food(2,"Eggs","Non_veg",52))
food_list.append(Food(3,"Olive oil","oil",120))
food_list.append(Food(4,"Onion","Veg",40))
food_list.append(Food(5,"Milk","dairy_food",52))

# list of operation to perfrom for EMRS app.
# Add the object into the list.

def create(food_obj):
    food_list.append(food_obj)
    return True;

# Update the food items:

def update(f_id,new_obj):
    old_obj = get(f_id)
    if old_obj is not None:
        index = food_list.index(old_obj)
        food_list[index] = new_obj
        return True

# Delete the food from the list:

def delete(f_id):
    filter_list = list(filter(lambda food_obj : food_obj.f_id == f_id,food_list))
    if len(filter_list) == 1:
        food_list.remove(filter_list[0])
        return True

# Show the food in the list:

def all():
    return food_list

# show food  by the id:

def show_id(f_id):
    filter_list = list(filter(lambda food_obj : food_obj.f_id == f_id,food_list))
    if len(filter_list) == 1:
        return filter_list[0]

# show the food by the name:

def show_name(f_name):
    filter_list = list(filter(lambda food_obj : food_obj.f_name == f_name,food_list))
    if len(filter_list) == 1:
        return filter_list[0]

# Show the food by its type :

def show_type(f_type):
    filter_list = list(filter(lambda food_obj : food_obj.f_type == f_type,food_list))
    if len(filter_list) == 1:
        return filter_list[0]
    

# Sort the food list by its name:

def sort_name():
    food_list.sort(key =lambda food_obj : food_obj.f_name)
    return food_list

# Sort the food list by its price:

def sort_price():
    food_list.sort(key = lambda food_obj : food_obj.f_price)
    return food_list







                       
