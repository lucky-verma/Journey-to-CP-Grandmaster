# Uses python3

import sys


def max_dot_product(a, b):
    # write your code here
    a.sort()
    b.sort()
    cn = []
    for i in range(n):
        cn.append(a[i] * b[i])
    return sum(cn)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(max_dot_product(a, b))
