# Dunder methods :- __init__, __str__, __repr__, __len__

class Car:
    brand = None
    model = None
    speed = None

    def __init__(self, brand, model, speed):

        self.brand = brand
        self.model = model
        self.speed = speed
    
    def __str__(self):

        return f"{self.brand} : {self.model} : {self.speed}"
    
    def __len__(self):
        return self.speed

bmw = Car("BMW1", "XI", 200)

print(bmw)
print(str(bmw))
print(len(bmw))