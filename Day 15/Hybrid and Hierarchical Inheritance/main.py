# Hybrid inheritance is a combination of multiple inheritance and single inheritance in object-oriented programming.


class BaseClass1:
  pass


class DerivedClass1(BaseClass1):
  pass


class DerivedClass2(BaseClass1):
  pass


class DerivedClass(DerivedClass1, DerivedClass2):
  pass


# Hierarchical Inheritance is a type of inheritance in Object-Oriented Programming where multiple subclasses inherit from a single base class. In other words, a single base class acts as a parent class for multiple subclasses. This is a way of establishing relationships between classes in a hierarchical manner.


class BaseClass:
  pass


class MangerClass1(BaseClass):
  pass


class MangerClass2(BaseClass):
  pass


class MangerClass3(BaseClass):
  pass
