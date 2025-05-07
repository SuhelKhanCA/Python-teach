class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes sound!")

class Dog(Animal):

    def __init__(self, name, breed):

        super().__init__(name) # calling parent constructor
        self.breed = breed

    def speak(self):
        print(f"{self.name} makes sound bow bow! and it has breed {self.breed}")


dg = Dog("Angara", "Labrador") # understand

dg.speak()