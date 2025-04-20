st = "You are a good boy"

dt = {}

for ch in st:

    dt[ch.lower()] = 0

#print(dt)

for ch in st:
    dt[ch.lower()] += 1


print(dt)