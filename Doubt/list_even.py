
def find_even_nums(ls):

    l = []

    for num in ls:

        if num % 2 == 0:
            l.append(num)

    return l


lis = [1, 2, 3, 4, 5, 6, 7, 8]

print(find_even_nums(lis))