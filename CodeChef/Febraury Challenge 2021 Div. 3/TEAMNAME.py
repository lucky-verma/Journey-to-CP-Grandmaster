# cook your dish here
def dis(x, y):
    s = len(set(x + y))
    return s


for _ in range(int(input())):
    n = int(input())
    lst = input().split()
    dict = {}
    for i in lst:
        k = i[1:]
        if k in dict:
            dict[k].append(i[0])
        else:
            dict[k] = [i[0]]
    dictN = list(dict.keys())
    s = 0
    for i in range(len(dict)):
        for l in range(i + 1, len(dict)):
            temp = dis(dict[dictN[i]], dict[dictN[l]])
            s += (temp - len(dict[dictN[i]])) * (temp - len(dict[dictN[l]]))
    print(2 * s)
