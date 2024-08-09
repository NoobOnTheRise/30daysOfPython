# Dictionaries are ordered collection of data items.
# They store multiple items in a single variable.
# Dictionary items are key-value pairs
# use - create a mapping

info = {'name': 'Karan', 'age': 19, 'eligible': True}
print(info)

print(info['name'])  # gives an error if key dosent exist
print(info.get('name'))

# access multiple keys
print(info.keys())
for key in info.keys():
    print(key)

# access multiple values
print(info.values())
for value in info.values():
    print(value)

# access key value pairs
print(info.items())
for key, value in info.items():
    print(key,value )
