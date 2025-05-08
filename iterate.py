# Iterate, Traverse

dt = {
    'a': 40,
    'b': 100
}

key1 = 'b'
key2 = 'c'

print(key1 in dt)
print(key2 in dt)

for key, val in dt.items():

    print(key, val)

for key in dt:

    print(key, dt[key])