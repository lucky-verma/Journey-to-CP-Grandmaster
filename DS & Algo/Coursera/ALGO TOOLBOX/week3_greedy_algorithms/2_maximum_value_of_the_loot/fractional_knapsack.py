# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    # write your code here
    value = 0
    for i in range(n):
        if capacity == 0:
            return value
        a = min(capacity, weights[values[i]])
        value += values[i] * a
        capacity -= a
    return value


if __name__ == "__main__":
    c = input()
    n, capacity = map(int, c.split())
    values = []
    weights = {}

    for i in range(n):
        c = input()
        v, w = map(int, c.split())
        values.append(v / w)
        weights[v / w] = w
    values.sort(reverse=True)

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
