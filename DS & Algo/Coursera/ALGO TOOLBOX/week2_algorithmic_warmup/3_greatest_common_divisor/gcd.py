# Uses python3
import sys


def gcd_fast(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd_fast(b, r)


if __name__ == "__main__":
    n = sys.stdin.read()
    # n = input()
    a, b = map(int, n.split())
    print(gcd_fast(a, b))
