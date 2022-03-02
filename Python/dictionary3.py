# with help of the dictionary we have created the list .
d1 = {101:18000,
      102:25000,
      103:22000,
      104:24000,
      105:15000
    }
sallist1 = [d1[i] for i in d1 if d1[i]>20000] # firdt method.
print(sallist1)
sallist2 = [i for i in d1.values() if i>20000] # second method.
print(sallist2)


#WAP to create dictionary using above list which values.
#but as key and its square as values.
l1 = [1,32,5,26,3]
d2 = {i:i**2 for i in l1}
print(d2)
