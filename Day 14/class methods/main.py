# One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary. 
# Another common use case for class methods as alternative constructors is when you want to create an object with a different set of default values than what is provided by the default constructor.
class Employee:
  def __init__(self, name, salary):
    self.name =  name
    self.salary = salary

  @classmethod
  def fromStr(cls, string):
    return cls(string.split("-")[0],string.split("-")[1])


string = "Menusha-120000".split("-")
b = Employee(string[0],string[1])
print(b.name," -------> ", b.salary)

string = "John-20000"
c = Employee.fromStr(string)
print(c.name," -------> ", c.salary)