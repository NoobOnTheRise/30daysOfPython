class Person:
  name = "Minal"
  occupation = "Software Developer"
  networth = 10

  # self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
  def info(self):
    print(self.name, self.occupation)


a = Person()
a.name = "Menusha"
a.occupation = "Incident Manager"
a.info()

b = Person()
b.name = "Anika"
b.occupation = "Lawyer"
b.info()

c = Person()
c.info()
