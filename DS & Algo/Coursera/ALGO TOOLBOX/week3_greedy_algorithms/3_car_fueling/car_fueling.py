# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    current = 0
    count = 0
    while current <= stops:
        last = current
        while current <= stops and distance[current + 1] - distance[last] <= m:
            current = current + 1
        if current == last:
            return -1
        if current <= stops:
            count = count + 1
    return count


if __name__ == '__main__':
    d = int(input())
    m = int(input())
    stops = int(input())
    i = input()
    distance = [0] + list(map(int, i.split())) + [d]
    print(compute_min_refills(distance, m, stops))
