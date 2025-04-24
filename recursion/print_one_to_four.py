def print_hello(n):

    if n == 5:
        return
    else:
        print("Hello world")
        print_hello(n+1)

print_hello(1)