

lst = []
print( " Enter the elements " ) 
for i in range(0,10):
    ele = int(input())
    lst.append(ele)
    print(lst)
    
smallest = largest = lst[0]

for i in range(0,10):
    if smallest > lst[i]:
        smallest = lst[i]
        #min_position = i

    if largest < lst[i]:
        largest = lst[i]
        #max_position = i

print( " Smallest number in this list is : " , smallest)
    
print( " Largest number in this list is : " , largest)
    
