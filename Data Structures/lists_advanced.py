l = [1,2,3,4,5]

for n in l:         #in checks for membership
    print(n)

print(1 in l)
print(50 in l)

print([n for n in l if n> 3])   #This combines the for loop and the if condition
print([n*2 for n in l])         #This goes ahead and multiplies all values in the list by 2