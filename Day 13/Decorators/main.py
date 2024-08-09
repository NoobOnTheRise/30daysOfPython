# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. 
# One common use of decorators is to add logging to a function.

def greet(fx):
  def mxf(*args, **kwargs):
    print("Good Morning")
    fx(*args, **kwargs)
    print("Thanks for using this function")
  return mxf

@greet # returns a function --> greet(hello)()
def hello():
  print("Hello World")

@greet #returns a function --> greet(add)(3,6)
def add(a,b):
  print(a+b)


hello()
add(3,6)