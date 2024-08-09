# Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes.


class Employee:

  def __init__(self, name):
    self.name = name

  def show(self):
    print(f"The name is {self.name}")


class Dancer:

  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is  {self.dance}")


class DancerEmployee(Employee, Dancer):

  def __init__(self, name, dance):
    self.name = name
    self.dance = dance

  def __str__(self):
    return f"{self.name} is a {self.dance} dancer"


o1 = DancerEmployee("Minal", "Break Dance")
print(o1)
print(o1.name)
print(o1.dance)
o1.show()
print(DancerEmployee.mro())

