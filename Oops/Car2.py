class Car:
    # var or members/attributes
    brand = None
    model = None
    speed = None

    def __init__(self, brand, model, speed):

        self.brand = brand
        self.model = model
        self.speed = speed
    # method
    def run(self):
        print(self.model, "running at : ", self.speed)


bmw = Car("BMW1", "XI", 200)
f1 = Car("Ford", "F-XUV", 150)

bmw.run()
f1.run()

# CW Animal -> name, lifespan, detail() -> name : lifespan ===> 3 objects