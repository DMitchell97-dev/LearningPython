l=[]
j = [1, 2, 3, 4, 5]
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(j[1])
print(j[-1])    #Negative reference is not bound by the usual start at 0 for arrays

j[0]=10
print(j[0])

print(j[0:2])   #Slicing uses the standard initial index and then end index is +1 of what you want

j[0:2] = [5, 6] #Slicing in new values to those indices
print(j[0:2])
print(j)

j[0:2] = [50, 60, 70, 80]   #Slices can also append data
print(j)

j[0:2] = []     #Slices can also be set to empty arrays to remove data
print(j)

l.append(6)
print(l)
l.append(7)
print(l)        #67676767676767676767676767676767676767676767676767676767
l.extend([8, 9])
print(l)
l.insert(0, 32)
print(l)

l.remove(32)    #Finds and remove the value from the list
print(l)
l.pop(2)        #Removes the element at the index
print(l)
#l.clear()      #Clears the list. duh
print(l.index(7))

l.reverse()
print(l)
l.sort()
print(l)
print(len(l))