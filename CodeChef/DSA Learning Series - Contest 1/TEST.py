ansOfLife = []
while True:
    x = int(input())
    if x == 42:
        break
    else:
        ansOfLife.append(x)
print(*ansOfLife, sep='\n')
