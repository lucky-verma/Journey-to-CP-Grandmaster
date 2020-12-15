for _ in range(int(input())):  # takes the input cases
    N, D = map(int, input().split())
    agesList = list(map(int, input().split()))
    risky, normal = 0, 0
    for k in agesList:
        if k <= 9 or k >= 80:
            risky = risky + 1
        else:
            normal = normal + 1
    rDay = risky // D
    nDay = normal // D
    if risky % D != 0:
        rDay = rDay + 1
    if normal % D != 0:
        rDay = rDay + 1
    rDay = rDay + nDay
    print(rDay)
