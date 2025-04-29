# sorting a list of tuples

ls =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 

# O/P : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

print(ls[0])
print(ls[0][1])

print(ls)


for i in range(0, len(ls)):

    for j in range(0, len(ls) - i - 1):

        if ls[j][1] > ls[j+1][1] : 

            temp = ls[j]
            ls[j] = ls[j+1]
            ls[j+1] = temp

print(ls)
