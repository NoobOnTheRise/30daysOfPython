# if else statement
age = int(input())
print("Your age is :", age)
# conditional operators
# >, < , >=, <=, ==, !=
if (age > 18):
  print("You can drive" )
else :
  print("You can't drive")

applePrice = 10
budget = 200

if (budget - applePrice > 50):
  print("Alexa, add 1 kg Apples to the cart.")
else:
  print("Alexa, do not add Apples to the cart.")

num = int(input())
print("Number is :", num)
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
else:
  print("Number is positive.")

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")