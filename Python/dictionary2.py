product = {'Id' : 1001,
           'Name':'Pen',
           'Price' : 15.0
           }
print(product)
# Set default(key,value= None).
# Used add new key with None as default values
product.setdefault('Quantity')
product.setdefault('M.date','25-AUG-2021')
print(product)
