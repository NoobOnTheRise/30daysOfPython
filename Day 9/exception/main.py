# Exception Handling
a = input("Enter the number: ")
print(f"multiplication of {a} is: ")
try:
  for i in range(1,11):
    print(f"{int(a)} * {i} = {int(a)*i}")
except Exception as e:
  print(e)

b = input("Enter the number: ")
print(f"multiplication of {b} is: ")
try:
  for i in range(1,11):
    print(f"{int(b)} * {i} = {int(b)*i}")
except ValueError:
  print("Number entered is not an integer")
except IndexError:
   print("Index error")