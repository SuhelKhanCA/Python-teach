# open, close, read -> str, or list

f = open('name.txt', 'a')

name1 = "\nAnas"
name2 = "\tTabassum Topper"
name3 = "\tAll people"


f.write(name1)
f.write(name2)
f.write(name3)

names = ['\nSuhel\n', 'Zainab\n', 'Parveen\n', 'Khusi\n', 'Keshvi\n']

f.writelines(names)

f.close()