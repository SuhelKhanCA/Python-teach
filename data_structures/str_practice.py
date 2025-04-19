#st = "somewhere"
st = "We have to go somewhere"
#print(len(st))
#print(st[0])

rev = ""

for i in range(0, len(st)):
    rev = st[i] + rev

print(rev)