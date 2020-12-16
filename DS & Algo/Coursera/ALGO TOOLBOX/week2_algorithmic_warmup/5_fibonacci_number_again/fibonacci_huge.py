# # Uses python3
# import sys
#
#
# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % m
#
#
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, m = map(int, input.split())
#     print(get_fibonacci_huge_naive(n, m))

# Use Python3

i = input()
n, m = map(int, i.split())

Fibo = [0, 1]
lastValue = [0, 1]

i = 2
last = 0
now = 1
while True:
    Fibo.append(Fibo[i - 1] + Fibo[i - 2])
    r = Fibo[i] % m
    lastValue.append(r)
    last = now
    now = r
    i = i + 1
    if [last, now] == [0, 1]:
        break

print(lastValue[n % (i-2)])