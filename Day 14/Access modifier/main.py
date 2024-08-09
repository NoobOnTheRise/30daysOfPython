# Access Specifiers/Modifiers -  limit the access of class variables and class methods 
# No private or public or protected in python


# public access modifier
class Student:
  # constructor is defined
  def __init__(self, age, name):
      self.age = age               # public variable
      self.name = name             # public variable

obj = Student(21,"Harry")
print(obj.age)
print(obj.name)

# private access modifier
# no strict concept of "private" access modifiers in python
# convention -variable or method should be considered private by prefixing its name with a double underscore (__)
class Student:
  # constructor is defined
  def __init__(self):
      self.__name = "Harry"               # private variable

obj = Student()
#print(obj.__name) #private variale - cannot be accessed directly
print(obj._Student__name) # name mangaling - indirectly access private attributes
# use of name mangling - prevents two unrelated classes from accidentally using the same name for an attribute.

# protected access modifier
# no strict concept of "protected" access modifiers in python
# indicating that a member is protected is to prefix its name with a single underscore (_)

class Student:
  def __init__(self):
      self._name = "Harry"

  def _funName(self):      # protected method
      return "CodeWithHarry"

class Subject(Student):       #inherited class
  pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())
#It's important to note that the single underscore is just a "naming convention", and does not actually provide any protection or restrict access to the member. The syntax we follow to make any variable protected is to write variable name followed by a single underscore (_) ie. _varName.