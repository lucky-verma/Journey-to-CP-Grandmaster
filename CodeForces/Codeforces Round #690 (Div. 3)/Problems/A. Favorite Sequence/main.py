"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""

if __name__ == "__main__":
    # Write your solution here
    for _ in range(int(input())):  # takes the input cases
        n = int(input())
        nonPolyCarpList = list(map(int, input().split()))
        polyCarpList = []
        for i in range(0, n // 2):
            polyCarpList.append(nonPolyCarpList[i])
            polyCarpList.append(nonPolyCarpList[n - i - 1])
        if n % 2 != 0:
            polyCarpList.append(nonPolyCarpList[n // 2])
        print(*polyCarpList)
    pass
