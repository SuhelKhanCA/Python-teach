def sum(*args):
    #print(args)
    sum=0
    for i in args:
        sum += i # sum = sum + i

    print(sum)


sum(2,3)
sum(3,4,5)
sum(23, 34,54,55)