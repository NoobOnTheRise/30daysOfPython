# super() keyword - used to refer to the parent class

class ParentClass1:
  def parent_method(self):
      print("This is the parent method of ParentClass1.")

class ChildClass(ParentClass1):
  def child_method(self):
      print("This is the child method.")
      super().parent_method()

child_object = ChildClass()
child_object.child_method()



class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programer(Employee):
  def __init__(self, name, id, lang):
    super().__init__(name, id)
    self.lang = lang

a = Employee(name="Rohit", id=123)
b = Programer(name="Minal", id=345, lang="Python")

print(a.name, b.name)