# Uses python3

import sys


def largest_number(data):
    # write your code here
    n = len(data)
    for i in range(n - 1):
        for i in range(n - 1 - i):
            if data[i] + data[i + 1] < data[i + 1] + data[i]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data


if __name__ == '__main__':
    n = int(input())
    data = list(input().split())

    digits = largest_number(data)
    result = ''
    for digit in digits:
        result += digit
    print(result)
