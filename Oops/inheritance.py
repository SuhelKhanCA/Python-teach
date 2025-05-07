
class A:

    a = 10
    b = 20

    def meth1(self):
        print("Parent class method")


class B(A):

    # a = 10
    # b = 20

    # def meth1()

    c = 30

    def meth2(self):
        print("Method of child class")


obj1 = B()

obj1.meth1()


# CW :

# Animal : name, lifespan, eat()

# Cat : softskin, meow()