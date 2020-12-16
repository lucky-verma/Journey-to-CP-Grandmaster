import sys


def fibonacci_partial_sum_fast(n):
    Fibo = [0, 1]
    last = [0, 1]
    for i in range(2, 60):
        Fibo.append(Fibo[i - 1] + Fibo[i - 2])
        last.append(int(str(Fibo[i])[-1]))

    q = int((n - m + 1) / 60)
    sum = 0
    for i in range((m + q * 60), (n + 1)):
        sum = sum + last[i % 60]

    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    m, n = map(int, input.split())
    print(fibonacci_partial_sum_fast(n))
