info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)

# The update() method updates the value of the key provided to it
# if the item already exists in the dictionary, else it creates a new key-value pair.

info.update({'age': 20})
info.update({'DOB': 2001})
print(info)

info.clear()
print(info)

# empty dic
empt = {}
print(empt)

#The pop() method removes the key-value pair whose key is passed as a parameter.
info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.pop('eligible')
print(info)

# The popitem() method removes the last key-value pair from the dictionary.
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
info.popitem()
print(info)

# del keyword - remove a dictionary item.
info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
del info['age']
print(info)
