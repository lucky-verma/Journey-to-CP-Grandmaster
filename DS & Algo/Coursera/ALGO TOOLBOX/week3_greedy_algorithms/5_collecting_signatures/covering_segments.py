# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    n = len(segments)
    current = 0
    ends = []
    while current < n:
        last = current
        while current < n - 1 and segments[current + 1][0] <= segments[last][1]:
            current = current + 1
            if segments[current][1] < segments[last][1]:
                last = current
        ends.append(segments[last][1])
        current = current + 1
    return ends


if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        ipt = input()
        segments.append(list(map(int, ipt.split())))
    segments.sort()
    points = optimal_points(segments)
    print(len(points))
    print(*points)
