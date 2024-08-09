# Walrus Operator - new addition to Python 3.8 and allows you to assign a value to a variable within an expression
# The Walrus Operator is represented by the := syntax

a = True
# print(a=False) will not work
print(a := False)

numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())

names = ["John", "Jane", "Jim"]

if (name := input("Enter a name: ")) in names:
    print(f"Hello, {name}!")
else:
    print("Name not found.")

foods = list()
while (food := input("What food do you like?: ")) != "quit":
    foods.append(food)
