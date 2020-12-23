"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""
from functools import reduce

if __name__ == "__main__":
    for _ in range(int(input())):
        """
        Option 1:
        """
        intList = list(map(int, input()))
        stack = []
        for k in intList:
            # stack.append(k)
            stack = [k] + stack
        s = reduce(lambda x, y: x + str(y), stack, '')
        print(s)
        """
        Option 2: This apparently seems to not print ending '0'
        """
        num = int(input())
        revNum = 0
        while num > 0:
            x = num % 10
            revNum = revNum * 10 + x
            num = num // 10
        print(revNum)
        """
        Option 3:
        """
        num = int(input())
        revNum = 0
        while num > 0:
            lastDigit = num % 10
            revNum = revNum * 10 + lastDigit
            num = num // 10
        print(revNum)
    pass
