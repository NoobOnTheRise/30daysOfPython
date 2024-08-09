# Single Inheritance - Single inheritance is a type of inheritance where a class inherits properties and behaviors from a single parent class

class Animal:
  def __init__(self, name, species):
      self.name = name
      self.species = species

  def make_sound(self):
      print("Sound made by the animal")


class Dog(Animal):
  def __init__(self, name, breed):
      Animal.__init__(self, name, species="Dog")
      self.breed = breed

  def make_sound(self):
      print("Bark!")

d = Dog("Dog", "Doberman")
d.make_sound()

a = Animal("Dog", "Dog")
a.make_sound()


# Quiz - Implement a cat class using Animal Class. Add some methods specific to cat

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed

    def make_sound(self):
        print("Meaow!")

    def play(self):
        print("Cat is playing.")

c = Cat("Cat", "Persian")
c.make_sound()



