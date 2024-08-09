# For loops

colors = ["Red", "Green", "Blue", "Yellow"]

for color in colors:
  print(color)
  
print("-----------")
name = 'Minal'

for letter in name:
  print(letter)

print("-----------")

for i in range(5,10):
  print(i)

print("-----------")
"""
The range() function takes three arguments:
1: The start value of the sequence (inclusive).
12: The end value of the sequence (exclusive).
3: The step size of the sequence. This indicates how much the sequence increments by for each value
"""
for i in range(1,12,3):
  print(i)