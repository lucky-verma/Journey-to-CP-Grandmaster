# Uses python3
import sys


def get_change(m):
    # write your code here
    changes = [10, 5, 1]
    c = 0
    for i in range(len(changes)):
        n = int(m / changes[i])
        c += n
        m -= n * changes[i]
    return c


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
