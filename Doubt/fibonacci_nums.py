# Fibo Seq : 0 , 1 , 1 , 2, 3, 5 ...

def find_fibo(n):

    l0 = 0
    l1 = 1
    print(l0)
    print(l1)

    for i in range(2, n-1):

        nex = l0 + l1
        l0 = l1
        l1 = nex

        print(nex)

find_fibo(10)

