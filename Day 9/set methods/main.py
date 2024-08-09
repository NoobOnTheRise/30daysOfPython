set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
#union() method returns a new set
#update() method adds item into the existing set from another set.
print(set1.union(set2))
set1.update(set2)
print(set1)
print(set2)

#  intersection() method returns a new set
# intersection_update() method updates into the existing set from another set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.intersection(cities2))
cities.intersection_update(cities2)
print(cities)

# symmetric_difference() method returns a new set
# symmetric_difference_update() method updates into the existing set from another set.

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities3 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.symmetric_difference(cities3))

# difference() method returns a new set
# difference_update() method updates into the existing set from another set.
cities4 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities5 = {"Seoul", "Kabul", "Delhi"}
cities6 = cities4.difference(cities5)
print(cities6)

cities7 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities8 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# isdisjoint() method checks if items of given set are present in another set.
print(cities7.isdisjoint(cities8))
# issuperset() method checks if all the items of a particular set are present in the original set.
print(cities7.issuperset(cities8))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Sri Lanka")
print(cities)

# remove vs discard - remove returns an error if the item is not present in the set.
# discard dose not returns an error if the item is not present in the set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
cities.discard("Sri Lanka")
print(cities)

# removes an element but its a random value that gets poped
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# del keyword deletes the entire set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
#print(cities)

# clear() method clears all items in the set and prints an empty set.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)

# You can also check if an item exists in the set or not.
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
