# Class variables - are attributes that are defined outside of instance methods and are shared by all instances of the class. They can be accessed using the class name, even if no instance of the class exists.
# Instance variables -  are attributes that are defined inside instance methods and are associated with each instance of a class. They can be accessed using the self parameter of the instance method

class Employee:
    companyName = "Apple"
    def __init__(self):
        self.name = "Minal"
        self.raiseAmt = 0.02

    def showInfo(self):
        print(f"The name of the employee is {self.name}. Works in {self.companyName}")

e = Employee()
Employee.companyName = "Google"
e.showInfo()
