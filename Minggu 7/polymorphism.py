class Parent:
    def __init__(self, lastName, eyeColor):
        print("Parent Constructor Called")
        self.lastName = lastName
        self.eyeColor = eyeColor

    def showInfo(self):
        print("Last Name - "+self.lastName)
        print("Eye Color - "+self.eyeColor)

class Child(Parent):
    def __init__(self, lastName, eyeColor, numberOfToys):
        print("Child Constructor Called")
        super().__init__(self, lastName, eyeColor)
        self.numberOfToys = numberOfToys

    def showInfo(self):
        print("Last Name - "+self.lastName)
        print("Eye Color - "+self.eyeColor)
        print("Number of Toys - "+str(self.numberOfToys))


child = Child("Qomar", "Merah", 5)
child.showInfo()