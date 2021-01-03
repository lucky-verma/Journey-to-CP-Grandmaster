# Uses python3
import sys


def optimal_summands(n):
    summands = []
    i = 0
    while n > 0:
        i = i + 1
        if n - i <= i:
            i = n
        summands.append(i)
        n = n - i
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
