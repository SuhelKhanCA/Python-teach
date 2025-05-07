class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes sound!")

class Dog(Animal):

    def speak(self):
        print(f"{self.name} makes bow bow!")

class Cat(Animal):

    def speak(self):
        print(f"{self.name} makes meow moew!")

an1 = Animal("Animal 1")
dg1 = Dog("Tommy")
ct1 = Cat("Tom")

an1.speak()
dg1.speak()
ct1.speak()