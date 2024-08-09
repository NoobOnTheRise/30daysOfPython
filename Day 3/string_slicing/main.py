# Strings
name = "Minal"
print("Hello, " + name)

print('He said, "I want to eat an apple".')

# Multiline Strings
a = """Hi my name is Minal
I am doing a 30 day Python challenge. 
Wish me Luck"""
print(a)

# Accessing Characters of a String
print(name[1])

# Looping through the string
for character in name:
  print(character)

names = "Minal,Shubham"
# Accessing part of the string
print(names[0:5])
# Slicing
print(names[:5])
print(names[5:])
print(names[:-3])
# Length of a string
print(len(names))

print("-------------------")
fruit = "Mango"
len1 = len(fruit)
print(len1)
print(fruit[0:4]) # include 0th value but not 4th value
print(fruit[:4]) # 0 will be applied automatically
print(fruit[:]) #len of fruit wil be applied
print(fruit[:-3]) # --> fruit[0:len(fruit)-3]
print(fruit[-1:-3]) # --> fruit[len(fruit)-1:len(fruit)-3]
print(fruit[-3:-1]) #--> fruit[len(fruit)-3:len(fruit)-1] --> 2:4

print("---------Quiz----------")
#Quick Quiz: 
nm = "Harry"
print(len(nm))
# Q: What will it print?
print(nm[-4:-2]) # -->nm[len(nm)-4:len(nm)-2] -> 1:3
# A: ar
