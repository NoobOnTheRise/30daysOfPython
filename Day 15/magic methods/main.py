# Magic Methods - special methods that you can define in your classes, and when invoked, they give you a powerful way to manipulate objects and their behaviour.

# __len__ - The len method is used to get the length of an object.

list = [0, 1, 2, 3, 4]

print(len(list))  # build in functions
print(list.__len__)


class Demo:

  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Name is {self.name}"

  def __len__(self):
    return len(self.name)

  def __call__(self, *args, **kwds):
    print("Hi")


d = Demo("Minal")
print(d)
print(len(d))
print(d())

# print all dunder/magic methods
print(dir(int))
