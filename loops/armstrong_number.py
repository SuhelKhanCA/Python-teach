n = 153
num = n
sum = 0

while num != 0:

    rem  = num % 10
    num = num // 10

    sum = sum + rem**3


if sum == n:
    print(n, "Yes it's an armstong number.")
else:
    print(n, "No, its not an armstrong number.")