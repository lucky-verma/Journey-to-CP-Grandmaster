# Uses python3
import sys


def fibonacci_sum_fast(n):
    F = [0, 1]
    last = [0, 1]
    for k in range(2, 60):
        F.append(F[k - 1] + F[k - 2])
        last.append(int(str(F[k])[-1]))
    sum = 2 * last[n % 60] + last[(n - 1) % 60] - 1

    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))
