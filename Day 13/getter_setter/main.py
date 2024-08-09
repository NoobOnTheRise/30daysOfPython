class MyClass:
  def __init__(self, value):
      ## private variables
      self._value = value

  def show(self):
        print(self._value)

  @property # getter
  def ten_value(self):
        return self._value*10

  @ten_value.setter # setter
  def ten_value(self, new_value):
        self._value = new_value/10


a = MyClass(10)
#a.value = 100
a.ten_value = 40
print(a.ten_value)
a.show()