l = [1,2,3]
t = (1,2,3)     #tuples are immutable and therefore a bit faster than list while being more rigid
print(t[0])
print(t[0:2])
#t[0] = 5       #This doesnt work because immutable

#td = {[1,2]: 1} #Lists can't be used as keys because lists can be changed and therefore are not hashable
td = {(1,2): 1}  #Tuples however can be used as a key for Dictionaries

def tuple_example():
    return 'apple', 'fruit', 2.00

fruit, kind, price = tuple_example()    #Tuples are often used for various data which makes it good for DB's
print(fruit, kind, price)