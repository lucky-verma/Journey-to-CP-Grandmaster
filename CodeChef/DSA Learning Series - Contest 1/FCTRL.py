for _ in range(int(input())):
    # n = int(input())
    # nLst = []
    # for i in range(n, 0, -1):
    #     nLst.append(i)
    # f = 1
    # for k in nLst:
    #     f = f * k
    # print(f)

    import math
    n = int(input())
    f = math.factorial(n)
    d = [str(x) for x in str(f)][::-1]
    c = 1
    for i in range(0, n):
        if d[i] == '0' and d[i + 1] == '0':
            c += 1
    print(c)
