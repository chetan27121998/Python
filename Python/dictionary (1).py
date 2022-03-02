'''
# Dictionary.
d1 = {1:'Raj',2:'Jay',3:'Sujay'}
print(d1)
d2 = {(12,3):123}# tuple type of key
print(d2)
d3 = {'EmpIds': [104,105,106],
      'EmpNames':['Raj','Jay','Rohit'],
      'EmpSal':[15000,52000,24000]
      }
print(d3)
print(d3['EmpIds'])
print(d3['EmpSal'])
'''
product = {'Id' : 1001,
           'Name':'Pen',
           'Price' : 15.0
           }
print(product)
print("Price:- Rs.",product['Price'])
product['Price'] = 20.0
print(product)
product['Description'] = 'Nice Pen'
print(product)
'''
del is implict operator of python which used
delete any exiting object/variable of python
'''
del product['Description']
print(product)

# Methods of dictionary.
# get the values of dictionary using its key.
print('Value of name:-',product.get('Name'))
print()
#get all the keys of dictionary.
print('Key of product dicitonary', product.keys())
#get all the values of dictionary.
print('Key of product dictionary', product.values())
#get all the pairs (key and value)of dictionary
#note:- this methods return tuple of key and values of each pair.
print("Items of product dictionary:-",product.items())
print()
# add item/pairs in dictionary using method.
#update method is used update dictionary object
p1 = {'Id': 1002,'Description': 'Nice pen'}
print(product)
print(p1)
product.update(p1)
print(product)
print()

# remove
'''
 1. pop(key):-
           used to remove pair of specificed key from the dictionary.
 2. pop item:-
           remove any pair from the dictionary and return it.
 3. clear:-
          remove all pairs from dictionary.
'''
product.pop('Price')
print(product)
item = product.popitem()
print(product)
print('Remove pair is:-',item)
print(product)
