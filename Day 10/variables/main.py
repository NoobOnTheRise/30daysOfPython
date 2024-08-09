# global vs local
# A local variable is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns.

# On the other hand, a global variable is a variable that is defined outside of a function and is accessible from within any function in your code.


x = 4 # global variable
print(x)

def hello():
  x = 5 # local variable
  print(x)
  print("Hello Minal")

hello()


x = 10 # global variable

def my_function():
  y = 5 # local variable
  print(y)

my_function()
print(x)
#print(y)  # this will cause an error because y is a local variable and is not accessible outside of the function

print("---------------------------------")

t = 10 # global variable
print(t)
def my_function1():
  global t # change the global variable from a function
  t = 5 # local variable
  print(t)

my_function1()
print(t)