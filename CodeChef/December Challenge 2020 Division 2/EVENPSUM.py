for _ in range(int(input())):  # takes the input cases
    A, B = map(int, input().split())
    xEven = A // 2
    xOdd = A - xEven
    yEven = B // 2
    yOdd = B - yEven
    print((xOdd * yOdd) + (yEven * xEven))
