# 123 => 321

# 121 => 121

num = 123
n  = num

sum = 0

while n != 0:

    dig = n % 10
    n = n // 10

    sum = sum * 10 + dig

print ("reverse is : ", sum)

