#unordered collection with no duplicate
#a = set()  #Create an empty set
#a = {}     #This doesn't create an empty set because dictionaries have priority on {} constructor
a = {1,2,3,4}   #This will generate a set with values
print(a)
a.add(4)
print(a)    #Print statement is the same since 4 is already in the set
a.add(5)
print(a)    #New value gets inserted

#Sets are collection of unique values

b = {4,5,6,7}
#Sets allow for additional data manipulation like finding all values between two sets or finding similarities
print(a & b)    #similar values
print(a | b)    #all the values