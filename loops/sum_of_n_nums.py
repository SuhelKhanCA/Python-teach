# n(n+1)/2

n = int(input("Enter nth number: "))

sum = 0
for i in range(1, n + 1):
    sum = sum + i

print("Sum for-loop", sum)


print("=======ALTERNATIVE========")

sum2 = 0
i = 1

while i <= n:
    sum2 = sum2 + i
    i = i + 1

print("sum while-loop", sum2)