# Bubble sort

lis = [23, 4, 56, 90, 1] # 1, 4, 23, 56, 90
print(lis)

for i in range(0, len(lis)):

    for j in range(0, len(lis) - i - 1):

        if lis[j] > lis[j+1] :
            
            temp = lis[j]
            lis[j] = lis[j+1]
            lis[j+1] = temp

print(lis)            
