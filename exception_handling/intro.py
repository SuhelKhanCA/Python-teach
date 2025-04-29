# Division

# a / b , b=0 -> exception


a = 10
b = 5

try:
    ans = a/b
    print(ans)

except ZeroDivisionError as e:
    print(str(e))

finally:
    print("It will always get excute!")