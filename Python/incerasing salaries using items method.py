'''
d1 = {101:18000,
      102:25000,
      103:22000,
      104:24000,
      105:15000
    }
d2 = {key:value+value*0.02 for key,value in d1.items()}
print(d1)
print(d2)
'''
radiuslist = [2.3,4.7,2.7,3]
newlist = {r:(value**2)*3.14 for r in radiuslist}
print(radiuslist)
print(newlist)
