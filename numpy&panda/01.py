import random

lis = [12 ,34, 54, 67 , 8]

# print(random.choice(lis))

print(random.random()) # 0 to 1

indx = int(random.random() * len(lis))

print(lis[indx])