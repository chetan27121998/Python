for row in range(1,5):
    for sp in range(1,row): #row = --> range(1,1)
        print(" ",end=" ")  #row = --> range(1,2)
    for star in range(4,row-1,-1):
        print(" * ",end=" ")
    print()
