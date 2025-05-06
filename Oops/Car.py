
class Car:
    brand = None
    model = None
    speed = None

    def __init__(self, brand, model, speed):

        self.brand = brand
        self.model = model
        self.speed = speed

bmw = Car("BMW1", "XI", 200)

print(bmw.brand)
print(bmw.model)
print(bmw.speed)