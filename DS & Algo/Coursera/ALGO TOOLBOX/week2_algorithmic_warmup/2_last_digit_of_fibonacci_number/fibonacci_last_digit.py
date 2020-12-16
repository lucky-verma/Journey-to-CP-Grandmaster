# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    F = [0, 1]
    last = [0, 1]
    for i in range(2, 60):
        F.append(F[i - 1] + F[i - 2])
        last.append(int(str(F[i])[-1]))

    return last[n % 60]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
