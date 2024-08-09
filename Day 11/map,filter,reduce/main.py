# Map - The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements.


def cube(x):
  return x * x * x


print(cube(2))
l = [1, 2, 4, 6, 4, 3]
newl = list(map(cube, l))
print(newl)


# Filter - The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and
def filter_func(a):
  return a > 3


filteredNewL = list(filter(filter_func, l))
print(filteredNewL)

# Reduce - The reduce function is a higher-order function that applies a function to a sequence and returns a single value.

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)
