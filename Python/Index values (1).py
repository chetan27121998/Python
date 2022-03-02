'''
L1 =[1,2,7,4,2,5]
index=L1.index(2)
print("Index of 2 is ",index)
index = L1.index(2,2)
print()
L1.remove(2)   # remove the first reference of the values.
print(L1)  
print()
L1.pop(-1) # POP function to 
print(L1)
print()
'''

#WAP to find second index of the value enterd by the user in the given list but print the index values.
L2 = [2,4,7,2,5,2,4]
element = int(input("Enter the values for find the second index: "))
if L2.count(element)!=0:
    if L2.count(element)>=2:
        index = L2.index(element,L2.index(element)+1)
        print("Element is found",index)# more than one time present in list.
    else:
        print("Element is present only once int the list")# one time present in list.
else:
    print("Element is not found")
print()

#WAP to find second index of the value enterd by the user in the given list.
L3 = [2,44,7,2,5,2,4,6,5,8]
element = int(input("Enter the values for find the second index: "))
if L3.count(element)!=0:
    if L3.count(element)>=2:
        print("Element is found")# more than one time present in list.
    else:
        print("Element is present only once int the list")# one time present in list.
else:
    print("Element is not found")

print()
# Sorting Function.
L4 = [1,5,6,9,7,8]
L4.sort()  # sort the values in ascending order by default.
print(L4)
L4.reverse() # reverse the values in list.
print(L4)
L4.sort(reverse=True) #using the both function output will be the descending order.
print(L4)
print()

#Coping function.
l1 = [1,2,3]
l2 = l1
l3 = l1.copy()
print(l1)
print(l2)
print(l3)
l1.pop(0)
print(l1)
print(l2)
print(l3)
print("Address of l1:",id(l1))
print("Address of l1:",id(l2))
print("Address of l1:",id(l3))
print("Is l1 is idential to l2",l1 is l2)
print("Is l1 is idential to l3",l1 is not l3)
