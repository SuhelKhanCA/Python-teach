
class Person:

    def __init__(self):
        self._legacy = "Big - W"
        self.__balance = "7 crore"


obj = Person()

# print(obj.__balance)
print(obj._Person__balance) # name magling