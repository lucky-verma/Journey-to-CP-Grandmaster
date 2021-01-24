def isNumeric(s):
    s = s.strip()
    try:
        s = float(s)
        return True
    except:
        return False


for _ in range(int(input())):
    s = input()
    lst = list(s)
    strict = lst[1:-1]
    size = len(s)
    num = []
    special = []
    lower = []
    upper = []
    if 10 <= size:
        for i in s:
            if i.islower():
                lower.append(i)
        for a in strict:
            if a.isupper():
                upper.append(a)
            if a.isnumeric():
                num.append(a)
            if a == '@' or a == '#' or a == '%' or a == '&' or a == '?':
                special.append(a)
        print(strict, len(num), len(special), len(lower), len(upper))
        if 0 < len(num) and 0 < len(special) and 0 < len(lower) and 0 < len(upper):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
