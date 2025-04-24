for i in range(0, 10):
    print(i)

print("=======")

def fxn(n):
    if n == 0:
        return
    fxn(n-1)
    print(n-1)

fxn(10)