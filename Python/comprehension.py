l1 = [24,6,7,4,17,45,90]
evenlist = []
for i in l1:
    if i%2==0:
        evenlist.insert(0,i) # (evenlist.append(i))
print(evenlist)

# list comprehension without condition.
evenlist1 = [i for i in l1]
print(evenlist1)
# list comprehension with condition.
sqevenlist1 = [i**2 for i in l1 if i%2==0]
print(sqevenlist1)

# set comprehension with condition.
sqevenlist1 = {i**2 for i in l1 if i%2==0}
print(sqevenlist1)
