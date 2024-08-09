# tuple operations
countries =  ["Spain", "India","Sri Lanka", "USA", "UK"]
countries2 =  ["Vietname", "China", "Japan"]
# concatenating two tuples
world = countries+ countries2
print(world)
# count the number of times an item appears in a tuple
tupNum = (1,3,4,5,3,3,7,4,9,5,3,4)
print("Count", tupNum.count(3))
# find the index of an item in a tuple
print("index of 3: ", tupNum.index(3))
"""
The index() method can take one to three parameters:

element - the item to scan
start_index (optional) - start scanning the element from the start_index
end_index (optional) - stop scanning the element at the end_index"""

alphabets = ('a', 'e', 'i', 'o', 'g', 'l', 'i', 'u')

# scans 'i' from index 4 to 7 and returns its index
index = alphabets.index('i', 4, 7)

print('Index of i in alphabets from index 4 to 7:', index)