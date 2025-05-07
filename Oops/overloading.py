# Overloading is not supported in Python

def sum(a, b):
    return a + b


def sum(a, b, c):
    return a + b + c

# print(sum(12, 12)) # Error
print(sum(12, 10, 5))