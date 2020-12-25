size = int(input())
values = [int(input()) for _ in range(size)]
values.sort()
countList = []
for k in range(0, size):
    count = 0
    for i in range(0, size):
        if values[i] - values[k] >= 0:
            count += 1
    countList.append(count * values[k])
print(max(countList))

"""
option 2: 
"""
num = int(input())
arr = []
for i in range(0, num):
    arr.append(int(input()))
m = 0
arr.sort()
for i in arr:
    if m < i * num:
        m = i * num
    num = num - 1
print(m)
