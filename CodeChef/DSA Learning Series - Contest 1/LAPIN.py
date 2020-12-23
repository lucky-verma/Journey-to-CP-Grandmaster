"""
Accomplished using the EduTools plugin by JetBrains https://plugins.jetbrains.com/plugin/10081-edutools
"""
from collections import Counter

if __name__ == "__main__":
    for _ in range(int(input())):
        """
        Option 1: 
        """
        wordList = list(input())
        if len(wordList) % 2 == 0:
            a = firstHalf = []
            for k in wordList[:len(wordList) // 2]:
                a.append(k)
            b = secondHalf = list((Counter(wordList) - Counter(a)).elements())
            c = list((Counter(a) - Counter(b)).elements())
            if len(c) == 0:
                print('YES')
            else:
                print('NO')
        elif len(wordList) % 2 == 1:
            del wordList[len(wordList) // 2]
            a = firstHalf = []
            for k in wordList[:len(wordList) // 2]:
                a.append(k)
            b = secondHalf = list((Counter(wordList) - Counter(a)).elements())
            c = list((Counter(a) - Counter(b)).elements())
            if len(c) == 0:
                print('YES')
            else:
                print('NO')

        """
        Option 2: 
        """
        s = input()
        if len(s) % 2 == 0:
            s1 = s[:(len(s) // 2)]
            s2 = s[(len(s) // 2):]
            p1 = ''.join(sorted(s1))
            p2 = ''.join(sorted(s2))
            if p1 == p2:
                print("YES")
            else:
                print("NO")
        else:
            s1 = s[:(len(s) // 2)]
            s2 = s[(len(s) // 2) + 1:]
            p1 = ''.join(sorted(s1))
            p2 = ''.join(sorted(s2))
            if p1 == p2:
                print("YES")
            else:
                print("NO")

        """
        Option 3:
        """

    pass
