#constructor is a special method in a class used to create and initialize an object of a class.
#Types of Constructors in Python
#   1. Parameterized Constructor
#   2. Default Constructor

class Person:
  name = "Minal"
  occupation = "Software Developer"
  networth = 10
  def __init__(self, name, occupation):

     self.name =  name;
     self.occupation =  occupation;


  # self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
  def info(self):
    print(self.name,"is a", self.occupation)


a = Person("Menusha", "Incident Manager")
a.info()
b = Person("Minal","Data Scientist")
b.info()
# a.name = "Menusha"
# a.occupation = "Incident Manager"
# a.info()