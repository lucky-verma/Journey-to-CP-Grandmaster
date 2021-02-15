# cook your dish here
n = int(input())
divsList = []


def printDivisors(n):
    i = 1
    while i <= n:
        if (n % i == 0):
            divsList.append(i)
        i = i + 1


printDivisors(n)
uptoTen = [i for i in divsList if i < 11]
print(uptoTen[-1])
