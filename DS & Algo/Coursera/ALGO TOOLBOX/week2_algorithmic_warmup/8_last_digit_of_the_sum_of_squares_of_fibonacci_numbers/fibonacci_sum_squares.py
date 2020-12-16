import sys


def fibonacci_partial_sum_fast(n):
    Fibo = [0, 1]
    last = [0, 1]
    for i in range(2, 60):
        Fibo.append(Fibo[i - 1] + Fibo[i - 2])
        last.append(int(str(Fibo[i])[-1]))
    square = last[n % 60] * last[n % 60] + last[n % 60] * last[(n - 1) % 60]

    return square % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_partial_sum_fast(n))
