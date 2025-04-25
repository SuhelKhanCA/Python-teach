# File handling : I/P and O/P -> File

f = open('name.txt', 'r')
# f = open('c:\\Users\\suhel\\Documents\\GitHub\\Python-teach\\file_handling\\name.txt', 'r')

print(type(f))

names = f.read()
print(type(names))
print(names)

names2 = f.readlines()
print(names2)


f.close()