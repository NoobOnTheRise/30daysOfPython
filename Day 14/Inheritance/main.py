# Inheritance  - class derives from another class
# Types -
# Single inheritance
# Multiple inheritance
# Multilevel inheritance
# Hierarchical Inheritance
# Hybrid Inheritance


class Employee:

  def __init__(self, name, id):
    self.name =  name
    self.id = id

  def showDetails(self):
    print(self.name, self.id)


class Programmer(Employee):

  def showLang(self):
    print("The default language is Python")



a = Employee("Minal", 1)
a.showDetails()

b = Programmer("Menusha", 2)
b.showDetails()
b.showLang()