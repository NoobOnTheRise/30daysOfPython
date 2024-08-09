"""
A tuple is a collection similar to a Python list. The primary difference is that we cannot modify a tuple once it is created."""
tup = (1,5,6,6)
print(type(tup), tup)
print(tup[2])
tup = (1,)
print(tup)
tup = (1,6,7,8)
print(tup[-1]) # len(tup) - 1)

if 6 in tup:
    print("Yes 6 is present in this tuple")

tup2 = tup[1:4] # creates a new tuple
print(tup2)