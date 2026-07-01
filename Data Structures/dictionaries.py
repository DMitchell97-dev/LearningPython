#Dictionaries are Maps basically

d = {'apple': 2, 'pear': 3, 'banana': 4}
print(d['pear'])    #Returns the value from the key
d['blueberry'] = 1  #Creates a new key, value pair
print(d.keys())     #Returns all the keys as a Tuple
print(d.values())   #Returns all values as a Tuple

l = list(d.keys())  #We have to cast it to a list if we want to return keys/values as a list
print(l)

print(d.get('apple', 'default'))
d.pop('apple')
print(d)

for k, v in d.items():
    print(k, v)

print({k.upper(): v*2 for k, v in d.items()})